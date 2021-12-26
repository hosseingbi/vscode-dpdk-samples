cmake_minimum_required(VERSION 3.0.0)
project(pktgen VERSION 0.1.0)

include(CTest)
enable_testing()

set(PKTGEN_PATH /usr/src/Pktgen-DPDK)

add_executable(pktgen ../app/cli-functions.c 
                      ../app/lpktgenlib.c 
                      ../app/pktgen-arp.c 
                      ../app/pktgen-capture.c 
                      ../app/pktgen-cfg.c 
                      ../app/pktgen-cmds.c 
                      ../app/pktgen-cpu.c 
                      ../app/pktgen-display.c 
                      ../app/pktgen-dump.c 
                      ../app/pktgen-ether.c 
                      ../app/pktgen-gre.c 
                      ../app/pktgen-gtpu.c 
                      ../app/pktgen-ipv4.c 
                      ../app/pktgen-ipv6.c 
                      ../app/pktgen-latency.c 
                      ../app/pktgen-log.c 
                      ../app/pktgen-main.c 
                      ../app/pktgen-pcap.c 
                      ../app/pktgen-port-cfg.c 
                      ../app/pktgen-random.c 
                      ../app/pktgen-range.c 
                      ../app/pktgen-rate.c 
                      ../app/pktgen-seq.c 
                      ../app/pktgen-stats.c 
                      ../app/pktgen-tcp.c 
                      ../app/pktgen-udp.c 
                      ../app/pktgen-vlan.c 
                      ../app/pktgen.c 
                      ../lib/common/cksum.c 
                      ../lib/common/cmdline_parse_args.c 
                      ../lib/common/copyright_info.c  
                      ../lib/common/core_info.c 
                      ../lib/common/coremap.c 
                      ../lib/common/l2p.c 
                      ../lib/common/lscpu.c 
                      ../lib/common/pg_pcap.c 
                      ../lib/common/pg_strings.c 
                      ../lib/common/port_config.c 
                      ../lib/common/utils.c 
                      ../lib/plugin/plugin.c
                      ../lib/utils/_atoip.c 
                      ../lib/utils/heap.c 
                      ../lib/utils/portlist.c 
                      ../lib/cli/cli_auto_complete.c 
                      ../lib/cli/cli_cmap.c 
                      ../lib/cli/cli_cmds.c 
                      ../lib/cli/cli_env.c 
                      ../lib/cli/cli_file.c 
                      ../lib/cli/cli_gapbuf.c 
                      ../lib/cli/cli_help.c 
                      ../lib/cli/cli_history.c 
                      ../lib/cli/cli_input.c 
                      ../lib/cli/cli_map.c 
                      ../lib/cli/cli_scrn.c 
                      ../lib/cli/cli_search.c 
                      ../lib/cli/cli_vt100.c 
                      ../lib/cli/cli.c 
                      ../lib/lua/lua_config.c  
                      ../lib/vec/vec.c)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

list(APPEND PKTGEN_INCLUDE_PATHS ../lib/cli)
list(APPEND PKTGEN_INCLUDE_PATHS ../lib/common)
list(APPEND PKTGEN_INCLUDE_PATHS ../lib/utils)
list(APPEND PKTGEN_INCLUDE_PATHS ../lib/lua)
list(APPEND PKTGEN_INCLUDE_PATHS ../lib/plugin)
list(APPEND PKTGEN_INCLUDE_PATHS /usr/local/include)


set(DPDK_BASE_PATH "/usr/src/dpdk-21.11")
set(DPDK_LIB_DIR "${DPDK_BASE_PATH}/build/lib")
set(DPDK_DRIVERS_LIB_DIR "${DPDK_BASE_PATH}/build/drivers")


set(DPDK_LIBS rte_node rte_graph rte_bpf rte_flow_classify rte_pipeline rte_table rte_port rte_fib rte_ipsec rte_vhost rte_stack 
                             rte_security rte_sched rte_reorder rte_rib rte_regexdev rte_rawdev rte_pdump rte_power rte_member rte_lpm rte_latencystats 
                             rte_kni rte_jobstats rte_ip_frag rte_gso rte_gro rte_eventdev rte_efd rte_distributor rte_cryptodev rte_compressdev rte_cfgfile 
                             rte_bitratestats rte_bbdev rte_acl rte_timer rte_hash rte_metrics rte_cmdline rte_pci rte_ethdev rte_meter rte_net rte_mbuf 
                             rte_mempool rte_rcu rte_ring rte_eal rte_telemetry rte_kvargs)


set(DPDK_DRIVER_LIBS rte_common_cpt rte_common_dpaax rte_common_iavf rte_common_octeontx rte_common_octeontx2 rte_bus_auxiliary rte_bus_dpaa rte_bus_fslmc 
                                    rte_bus_ifpga rte_bus_pci rte_bus_vdev rte_bus_vmbus rte_common_cnxk rte_common_qat rte_common_sfc_efx rte_mempool_bucket rte_mempool_cnxk 
                                    rte_mempool_dpaa rte_mempool_dpaa2 rte_mempool_octeontx rte_mempool_octeontx2 rte_mempool_ring rte_mempool_stack rte_net_af_packet 
                                    rte_net_ark rte_net_atlantic rte_net_avp rte_net_axgbe rte_net_bnxt rte_net_bond rte_net_cnxk rte_net_cxgbe rte_net_dpaa rte_net_dpaa2 
                                    rte_net_e1000 rte_net_ena rte_net_enetc rte_net_enic rte_net_failsafe rte_net_fm10k rte_net_hinic rte_net_hns3 rte_net_i40e rte_net_iavf 
                                    rte_net_ice rte_net_igc rte_net_ionic rte_net_ixgbe rte_net_kni rte_net_liquidio rte_net_memif rte_net_netvsc rte_net_nfp rte_net_ngbe 
                                    rte_net_null rte_net_octeontx rte_net_octeontx2 rte_net_octeontx_ep rte_net_pcap rte_net_pfe rte_net_qede rte_net_ring rte_net_softnic 
                                    rte_net_tap rte_net_thunderx rte_net_txgbe rte_net_vdev_netvsc rte_net_vhost rte_net_virtio rte_net_vmxnet3 rte_raw_cnxk_bphy rte_raw_dpaa2_cmdif 
                                    rte_raw_dpaa2_qdma rte_raw_ntb rte_raw_skeleton rte_crypto_bcmfs rte_crypto_caam_jr 
                                    rte_crypto_cnxk rte_crypto_dpaa_sec rte_crypto_dpaa2_sec rte_crypto_nitrox rte_crypto_null rte_crypto_octeontx rte_crypto_octeontx2 
                                    rte_crypto_scheduler rte_crypto_virtio rte_compress_octeontx rte_regex_octeontx2 rte_vdpa_ifc rte_event_cnxk rte_event_dlb2 rte_event_dpaa 
                                    rte_event_dpaa2 rte_event_dsw rte_event_octeontx2 rte_event_opdl rte_event_skeleton rte_event_sw rte_event_octeontx rte_baseband_acc100 
                                    rte_baseband_fpga_5gnr_fec rte_baseband_fpga_lte_fec rte_baseband_null rte_baseband_turbo_sw)

set(EXTRA_LIBS pthread m dl numa pcap)

list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/eal/include/)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/config/)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/eal/linux/include/)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/eal/x86/include)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/eal/common)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/eal)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/kvargs )
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/metrics)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/telemetry)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/mempool)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/ring)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/net)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/mbuf)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/ethdev)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/meter)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/cmdline)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/pci)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/hash)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/timer)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/rcu)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/lib/lpm)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/drivers/net/bonding)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/drivers/bus/pci)
list(APPEND DPDK_INCLUDE_PATHS ${DPDK_BASE_PATH}/build)

set(DPDK_DEFS _FILE_OFFSET_BITS=64 _GNU_SOURCE ALLOW_EXPERIMENTAL_API)

set(DPDK_FLAGS "-pipe -Wall -Winvalid-pch -O3 -include rte_config.h -Wextra -Wcast-qual -Wdeprecated -Wformat -Wformat-nonliteral -Wformat-security -Wmissing-declarations -Wmissing-prototypes -Wnested-externs -Wold-style-definition -Wpointer-arith -Wsign-compare -Wstrict-prototypes -Wundef -Wwrite-strings -Wno-missing-field-initializers -D_GNU_SOURCE -march=native -MD -MQ")

target_include_directories(pktgen PRIVATE . ${DPDK_INCLUDE_PATHS} ${PKTGEN_INCLUDE_PATHS})
target_link_directories(pktgen PRIVATE ${DPDK_LIB_DIR} ${DPDK_DRIVERS_LIB_DIR})
target_link_libraries(pktgen -Wl,--no-undefined -Wl,-O1 -Wl,--whole-archive -Wl,--start-group ${DPDK_LIBS} ${DPDK_DRIVER_LIBS}  
                        -Wl,--no-whole-archive ${EXTRA_LIBS} -Wl,--end-group )
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${DPDK_FLAGS} -g3" )
target_compile_definitions(pktgen PRIVATE ${DPDK_DEFS} __PROJECT_VERSION="21.11.0")