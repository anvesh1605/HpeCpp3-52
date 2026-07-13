# Source Check Sheet

Use this as a quick rerun list for the grounded terminal QA flow.

Note:
- Questions 4 and 5 say "route scale", but the official sources describe route-capacity limits, not VSF member range.
- Question 1 does not appear as a literal "standalone ISSU" fact in the docs I found. The closest verified source-backed fact is VSF ISSU on 6300.

| # | Question | Selected Context | Verified Answer | Source |
|---|---|---|---|---|
| 1 | Which are the AOSCX Switches support Standalone ISSU? | `6300` / `VSF ISSU` | VSF ISSU is supported only on the HPE Aruba Networking 6300 Switch Series, except S3L75A, S3L76A, and S3L77A. | [AOS-CX 10.16 VSF Guide](https://arubanetworking.hpe.com/techdocs/AOS-CX/10.16/PDF/vsf.pdf) |
| 2 | Since which version 4100 supports VSF? | `4100` / `VSF guide` | `10.16.1000` | [AOS-CX 10.16 VSF Guide](https://arubanetworking.hpe.com/techdocs/AOS-CX/10.16/PDF/vsf.pdf) |
| 3 | How can I bring up a 6300 in VSX mode? | `VSX keepalive peer` / `VSX setup` | Configure the keepalive peer on both switches, route it over L3, and do not run it over the ISL. | [keepalive peer](https://arubanetworking.hpe.com/techdocs/AOS-CX/10.16/HTML/vsx/Content/VSX_cmds/kee-pee-10.htm), [Configuring core 1 and core 2 for VSX](https://arubanetworking.hpe.com/techdocs/AOS-CX/10.16/HTML/vsx/Content/Chp_Setup/cnf-cor-1-cor-2-10.htm) |
| 4 | What is the supported route scale on 6200? | `6200` / `route capacity` | The number of IPv4 and IPv6 static routes that can be configured is limited to 1024 combined. 16K routes are not supported. | [AOS-CX 10.14 IP Routing Guide (6200)](https://arubanetworking.hpe.com/techdocs/AOS-CX/10.14/HTML/ip_route_4100i-6000-6100-6200/Content/Chp_StatRoute/cnf-exa-pro.htm) |
| 5 | What is the supported route scale for Aruba 6300 switch in AOS-CX 10.16? | `6300` / `route capacity` | The number of IPv4 and IPv6 static routes that can be configured is limited to 16K combined. | [AOS-CX 10.16 IP Routing Guide (6300, 6400, 8100, 83xx, 93xx, 100xx)](https://arubanetworking.hpe.com/techdocs/AOS-CX/10.16/PDF/ip_route_6300-6400-8100-83xx-9300-10000.pdf) |
| 6 | For 8320 AOS-CX 10.06, what is the output of the `show ip route`? | `show ip route` / canonical output example | `Displaying ipv4 routes selected for forwarding` followed by the documented IPv4 route table example. | [AOS-CX 10.13 IP Routing Guide](https://arubanetworking.hpe.com/techdocs/AOS-CX/10.13/PDF/ip_route_8400.pdf) |

## Quick rerun prompt set

Run these in the terminal QA tool with the selected context shown in the table:

1. `Which are the AOSCX Switches support Standalone ISSU?`
2. `Since which version 4100 supports VSF?`
3. `How can I bring up a 6300 in VSX mode?`
4. `What is the supported route scale on 6200?`
5. `What is the supported route scale for Aruba 6300 switch in AOS-CX 10.16?`
6. `For 8320 AOS-CX 10.06, what is the output of the show ip route?`
