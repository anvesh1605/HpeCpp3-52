#!/usr/bin/env python3
"""
Calculate accuracy metrics on test results
- ROUGE-L (Longest Common Subsequence overlap)
- BLEU Score (N-gram precision)
- CLI Score (Command token similarity)
- Hallucination Score (Context grounding)
- Keyword Accuracy (Domain terms coverage)
- Bug Similarity (Combined score)
"""
import json
from pathlib import Path
from collections import defaultdict
import re
from typing import Dict, List, Tuple

# Domain keywords from METRICS_AND_RUNGUIDE.md
DOMAIN_KEYWORDS = {
    'crash', 'reboot', 'hang', 'deadlock', 'race condition', 'snmp', 'mib', 
    'vlan', 'lag', 'stp', 'evpn', 'bgp', 'rest', 'ovsdb', 'pvst', 'mvrp', 
    'lldp', 'vsx', 'radius', 'blocked', 'disabled', 'nan'
}

# CLI command tokens to extract
CLI_TOKENS = {'show', 'configure', 'interface', 'vlan', 'ip', 'command', 'config', 'port', 'enable', 'disable'}


def longest_common_subsequence(s1: str, s2: str) -> float:
    """Calculate ROUGE-L score using Longest Common Subsequence"""
    s1_words = s1.lower().split()
    s2_words = s2.lower().split()
    
    m, n = len(s1_words), len(s2_words)
    if m == 0 or n == 0:
        return 0.0
    
    # Build LCS table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1_words[i-1] == s2_words[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    lcs_len = dp[m][n]
    rouge_l = 2.0 * lcs_len / (m + n) if (m + n) > 0 else 0.0
    return min(1.0, rouge_l)


def bleu_score(prediction: str, reference: str, n_gram: int = 4) -> float:
    """Calculate BLEU score (N-gram precision)"""
    pred_words = prediction.lower().split()
    ref_words = reference.lower().split()
    
    if len(pred_words) == 0 or len(ref_words) == 0:
        return 0.0
    
    # Calculate n-gram matches
    score = 0.0
    for n in range(1, min(n_gram + 1, len(pred_words) + 1)):
        pred_ngrams = set()
        ref_ngrams = set()
        
        for i in range(len(pred_words) - n + 1):
            pred_ngrams.add(' '.join(pred_words[i:i+n]))
        
        for i in range(len(ref_words) - n + 1):
            ref_ngrams.add(' '.join(ref_words[i:i+n]))
        
        matches = len(pred_ngrams & ref_ngrams)
        total = len(pred_ngrams)
        
        if total > 0:
            score += matches / total / n_gram
    
    return min(1.0, score)


def cli_score(prediction: str, reference: str) -> float:
    """Calculate CLI token similarity score"""
    # Extract CLI tokens
    pred_tokens = set()
    ref_tokens = set()
    
    for token in CLI_TOKENS:
        if token in prediction.lower():
            pred_tokens.add(token)
        if token in reference.lower():
            ref_tokens.add(token)
    
    if len(ref_tokens) == 0:
        return 1.0 if len(pred_tokens) == 0 else 0.0
    
    matches = len(pred_tokens & ref_tokens)
    cli_sim = matches / len(ref_tokens)
    
    return min(1.0, cli_sim)


def hallucination_score(prediction: str, context: str, question: str) -> float:
    """
    Calculate hallucination score - check if identifiers are grounded in context
    Looks for Bug IDs, firmware versions that appear in prediction
    """
    # Extract Bug IDs from prediction (format: Bug ID XXXXXX or BUGID-XXXXXX)
    pred_bugs = set(re.findall(r'(?:Bug ID|BUGID)[:\s-]+(\d+)', prediction, re.IGNORECASE))
    
    # Extract from context+question
    context_text = context + " " + question
    context_bugs = set(re.findall(r'(?:Bug ID|BUGID)[:\s-]+(\d+)', context_text, re.IGNORECASE))
    
    # Extract firmware versions from prediction
    pred_versions = set(re.findall(r'\d+[._]\d+[._]?\d*', prediction))
    context_versions = set(re.findall(r'\d+[._]\d+[._]?\d*', context_text))
    
    # Calculate grounding score
    total_identifiers = len(pred_bugs) + len(pred_versions)
    if total_identifiers == 0:
        return 1.0  # No hallucination if no identifiers mentioned
    
    grounded = 0
    for bug in pred_bugs:
        if bug in context_bugs:
            grounded += 1
    
    for version in pred_versions:
        if version in context_versions:
            grounded += 1
    
    hallucination = grounded / total_identifiers if total_identifiers > 0 else 1.0
    return min(1.0, hallucination)


def keyword_accuracy(prediction: str) -> float:
    """Calculate keyword accuracy - fraction of domain keywords present"""
    pred_lower = prediction.lower()
    found_keywords = sum(1 for kw in DOMAIN_KEYWORDS if kw in pred_lower)
    
    if len(DOMAIN_KEYWORDS) == 0:
        return 0.0
    
    return found_keywords / len(DOMAIN_KEYWORDS)


def bug_similarity(prediction: str, reference: str, question: str) -> float:
    """
    Calculate bug similarity score
    Formula: 0.7 * keyword_accuracy + 0.3 * length_ratio
    """
    kw_acc = keyword_accuracy(prediction)
    
    pred_len = len(prediction.split())
    ref_len = len(reference.split())
    
    if ref_len == 0:
        length_ratio = 1.0 if pred_len == 0 else 0.0
    else:
        length_ratio = min(pred_len, ref_len) / max(pred_len, ref_len)
    
    return 0.7 * kw_acc + 0.3 * length_ratio


def calculate_metrics(prediction: str, reference: str, context: str = "", question: str = "") -> Dict[str, float]:
    """Calculate all metrics for a prediction-reference pair"""
    return {
        'rouge_l': longest_common_subsequence(prediction, reference),
        'bleu': bleu_score(prediction, reference),
        'cli_score': cli_score(prediction, reference),
        'hallucination': hallucination_score(prediction, context, question),
        'keyword_accuracy': keyword_accuracy(prediction),
        'bug_similarity': bug_similarity(prediction, reference, question),
    }


def load_test_results(filepath: str) -> List[Dict]:
    """Load test results from JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)


def analyze_results(results: List[Dict]) -> Dict:
    """Analyze all results and calculate aggregate metrics"""
    metrics_by_switch = defaultdict(lambda: defaultdict(list))
    metrics_by_question = defaultdict(lambda: defaultdict(list))
    all_metrics = defaultdict(list)
    
    for result in results:
        switch = result.get('switch', 'unknown')
        version = result.get('version', 'unknown')
        question = result.get('question', '')
        answer = result.get('answer', '')
        suggestions = result.get('suggestions', '')
        
        # Calculate metrics (using suggestions as reference since we don't have ground truth)
        metrics = calculate_metrics(answer, suggestions, "", question)
        
        # Aggregate by switch
        switch_key = f"{switch}/{version}"
        for metric_name, value in metrics.items():
            metrics_by_switch[switch_key][metric_name].append(value)
        
        # Aggregate by question
        for metric_name, value in metrics.items():
            metrics_by_question[question][metric_name].append(value)
        
        # All metrics
        for metric_name, value in metrics.items():
            all_metrics[metric_name].append(value)
    
    return {
        'by_switch': metrics_by_switch,
        'by_question': metrics_by_question,
        'all': all_metrics,
        'total_results': len(results)
    }


def calculate_summary(metric_list: List[float]) -> Dict[str, float]:
    """Calculate summary statistics for a metric"""
    if not metric_list:
        return {'mean': 0.0, 'min': 0.0, 'max': 0.0, 'std': 0.0}
    
    mean = sum(metric_list) / len(metric_list)
    min_val = min(metric_list)
    max_val = max(metric_list)
    variance = sum((x - mean) ** 2 for x in metric_list) / len(metric_list) if len(metric_list) > 0 else 0.0
    std = variance ** 0.5
    
    return {
        'mean': mean,
        'min': min_val,
        'max': max_val,
        'std': std,
        'count': len(metric_list)
    }


def generate_report(analysis: Dict) -> str:
    """Generate a comprehensive metrics report"""
    report = []
    report.append("\n" + "=" * 80)
    report.append("ACCURACY METRICS REPORT - HPE Aruba Switch Support Assistant")
    report.append("=" * 80 + "\n")
    
    # Overall metrics
    report.append("OVERALL METRICS (All Tests)")
    report.append("-" * 80)
    report.append(f"Total Test Results: {analysis['total_results']}\n")
    
    for metric_name in ['rouge_l', 'bleu', 'cli_score', 'hallucination', 'keyword_accuracy', 'bug_similarity']:
        values = analysis['all'][metric_name]
        summary = calculate_summary(values)
        report.append(f"{metric_name.upper()}")
        report.append(f"  Mean:  {summary['mean']:.4f}")
        report.append(f"  Min:   {summary['min']:.4f}")
        report.append(f"  Max:   {summary['max']:.4f}")
        report.append(f"  StdDev: {summary['std']:.4f}")
        report.append("")
    
    # By switch
    report.append("\n" + "=" * 80)
    report.append("METRICS BY SWITCH")
    report.append("=" * 80 + "\n")
    
    for switch_key in sorted(analysis['by_switch'].keys()):
        report.append(f"\n{switch_key}")
        report.append("-" * 40)
        
        for metric_name in ['rouge_l', 'bleu', 'cli_score', 'hallucination', 'keyword_accuracy', 'bug_similarity']:
            values = analysis['by_switch'][switch_key][metric_name]
            summary = calculate_summary(values)
            report.append(f"{metric_name:20s}: {summary['mean']:.4f} (±{summary['std']:.4f}) [{summary['min']:.4f} - {summary['max']:.4f}]")
    
    # By question
    report.append("\n" + "=" * 80)
    report.append("METRICS BY QUESTION")
    report.append("=" * 80 + "\n")
    
    for i, question in enumerate(sorted(analysis['by_question'].keys()), 1):
        report.append(f"\n{i}. {question[:60]}...")
        report.append("-" * 60)
        
        for metric_name in ['rouge_l', 'bleu', 'cli_score', 'hallucination', 'keyword_accuracy', 'bug_similarity']:
            values = analysis['by_question'][question][metric_name]
            summary = calculate_summary(values)
            report.append(f"{metric_name:20s}: {summary['mean']:.4f} (±{summary['std']:.4f})")
    
    # Threshold analysis
    report.append("\n" + "=" * 80)
    report.append("THRESHOLD ANALYSIS")
    report.append("=" * 80 + "\n")
    
    thresholds = {
        'rouge_l': 0.50,
        'bleu': 0.30,
        'cli_score': 0.70,
        'hallucination': 0.90,
        'keyword_accuracy': 0.75,
        'bug_similarity': 0.65
    }
    
    for metric_name, threshold in thresholds.items():
        values = analysis['all'][metric_name]
        above_threshold = sum(1 for v in values if v >= threshold)
        percentage = (above_threshold / len(values) * 100) if values else 0
        
        report.append(f"{metric_name:20s}")
        report.append(f"  Threshold: {threshold:.2f}")
        report.append(f"  Above Threshold: {above_threshold}/{len(values)} ({percentage:.1f}%)")
        report.append("")
    
    return "\n".join(report)


def main():
    results_file = "test_results_all_switches.json"
    
    print(f"Loading test results from {results_file}...")
    results = load_test_results(results_file)
    
    print(f"Analyzing {len(results)} test results...")
    analysis = analyze_results(results)
    
    print("Generating report...")
    report = generate_report(analysis)
    print(report)
    
    # Save report
    report_file = "metrics_report.txt"
    with open(report_file, 'w') as f:
        f.write(report)
    print(f"\nReport saved to {report_file}")
    
    # Save detailed metrics to JSON
    metrics_json = {
        'total_results': analysis['total_results'],
        'overall_metrics': {
            metric_name: calculate_summary(analysis['all'][metric_name])
            for metric_name in ['rouge_l', 'bleu', 'cli_score', 'hallucination', 'keyword_accuracy', 'bug_similarity']
        },
        'by_switch': {
            switch_key: {
                metric_name: calculate_summary(analysis['by_switch'][switch_key][metric_name])
                for metric_name in ['rouge_l', 'bleu', 'cli_score', 'hallucination', 'keyword_accuracy', 'bug_similarity']
            }
            for switch_key in analysis['by_switch'].keys()
        }
    }
    
    metrics_file = "metrics_summary.json"
    with open(metrics_file, 'w') as f:
        json.dump(metrics_json, f, indent=2)
    print(f"Metrics saved to {metrics_file}")


if __name__ == "__main__":
    main()
