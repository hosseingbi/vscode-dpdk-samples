cmake_minimum_required(VERSION 3.0.0)
project(trex VERSION 0.1.0)

include(CTest)
enable_testing()



# this should be set
set(TREX_CORE_PATH /usr/src/trex/trex-core)


add_executable(trex ${TREX_CORE_PATH}/src/bp_sim_stf.cpp
                    ${TREX_CORE_PATH}/src/bp_sim_tcp.cpp
                    ${TREX_CORE_PATH}/src/bp_sim.cpp
                    ${TREX_CORE_PATH}/src/debug.cpp
                    ${TREX_CORE_PATH}/src/dpdk_drv_filter.cpp 
                    ${TREX_CORE_PATH}/src/dpdk_port_map.cpp 
                    ${TREX_CORE_PATH}/src/dpdk_trex_port_attr.cpp 
                    ${TREX_CORE_PATH}/src/flow_stat_parser.cpp 
                    ${TREX_CORE_PATH}/src/global_io_mode.cpp 
                    ${TREX_CORE_PATH}/src/h_timer.cpp 
                    ${TREX_CORE_PATH}/src/inet_pton.cpp 
                    ${TREX_CORE_PATH}/src/main_dpdk.cpp 
                    ${TREX_CORE_PATH}/src/msg_manager.cpp 
                    ${TREX_CORE_PATH}/src/nat_check_flow_table.cpp 
                    ${TREX_CORE_PATH}/src/nat_check.cpp 
                    ${TREX_CORE_PATH}/src/os_time.cpp 
                    ${TREX_CORE_PATH}/src/pkt_gen.cpp 
                    ${TREX_CORE_PATH}/src/platform_cfg.cpp 
                    ${TREX_CORE_PATH}/src/pre_test.cpp 
                    ${TREX_CORE_PATH}/src/rx_check_header.cpp 
                    ${TREX_CORE_PATH}/src/rx_check.cpp 
                    ${TREX_CORE_PATH}/src/stateful_rx_core.cpp 
                    ${TREX_CORE_PATH}/src/stt_cp.cpp 
                    ${TREX_CORE_PATH}/src/time_histogram.cpp 
                    ${TREX_CORE_PATH}/src/timer_wheel_pq.cpp 
                    ${TREX_CORE_PATH}/src/trex_build_info.cpp 
                    ${TREX_CORE_PATH}/src/trex_client_config.cpp 
                    ${TREX_CORE_PATH}/src/trex_global.cpp 
                    ${TREX_CORE_PATH}/src/trex_modes.cpp 
                    ${TREX_CORE_PATH}/src/trex_platform.cpp 
                    ${TREX_CORE_PATH}/src/trex_port_attr.cpp 
                    ${TREX_CORE_PATH}/src/trex_watchdog.cpp 
                    ${TREX_CORE_PATH}/src/tuple_gen.cpp 
                    ${TREX_CORE_PATH}/src/tw_cfg.cpp 
                    ${TREX_CORE_PATH}/src/drivers/trex_driver_base.cpp 
                    ${TREX_CORE_PATH}/src/drivers/trex_driver_bnxt.cpp 
                    ${TREX_CORE_PATH}/src/drivers/trex_driver_i40e.cpp 
                    ${TREX_CORE_PATH}/src/drivers/trex_driver_igb.cpp 
                    ${TREX_CORE_PATH}/src/drivers/trex_driver_ixgbe.cpp 
                    ${TREX_CORE_PATH}/src/drivers/trex_driver_mlx5.cpp 
                    ${TREX_CORE_PATH}/src/drivers/trex_driver_ntacc.cpp 
                    ${TREX_CORE_PATH}/src/drivers/trex_driver_vic.cpp 
                    ${TREX_CORE_PATH}/src/drivers/trex_driver_virtual.cpp 
                    ${TREX_CORE_PATH}/src/drivers/trex_driver_ice.cpp
                    ${TREX_CORE_PATH}/src/publisher/trex_publisher.cpp 
                    ${TREX_CORE_PATH}/src/utils/utl_counter.cpp 
                    ${TREX_CORE_PATH}/src/utils/utl_cpuu.cpp 
                    ${TREX_CORE_PATH}/src/utils/utl_dbl_human.cpp 
                    ${TREX_CORE_PATH}/src/utils/utl_ip.cpp 
                    ${TREX_CORE_PATH}/src/utils/utl_json.cpp 
                    ${TREX_CORE_PATH}/src/utils/utl_mbuf.cpp 
                    ${TREX_CORE_PATH}/src/utils/utl_offloads.cpp 
                    ${TREX_CORE_PATH}/src/utils/utl_policer.cpp 
                    ${TREX_CORE_PATH}/src/utils/utl_port_map.cpp 
                    ${TREX_CORE_PATH}/src/utils/utl_sync_barrier.cpp 
                    ${TREX_CORE_PATH}/src/utils/utl_term_io.cpp 
                    ${TREX_CORE_PATH}/src/utils/utl_yaml.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_capture.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_dp_core.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_dp_port_events.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_latency_counters.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_messaging.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_owner.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_pkt.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_port.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_rpc_cmds_common.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_rx_core.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_rx_packet_parser.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_rx_port_mngr.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_rx_rpc_tunnel.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_rx_tx.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_stack_base.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_stack_counters.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_stack_legacy.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_stack_linux_based.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_stx.cpp 
                    ${TREX_CORE_PATH}/src/stx/common/trex_vlan_filter.cpp
                    ${TREX_CORE_PATH}/src/stx/common/trex_tpg_stats.cpp
                    ${TREX_CORE_PATH}/src/stx/stf/trex_stf.cpp 
                    ${TREX_CORE_PATH}/src/stx/stl/trex_stl_dp_core.cpp 
                    ${TREX_CORE_PATH}/src/stx/stl/trex_stl_fs.cpp 
                    ${TREX_CORE_PATH}/src/stx/stl/trex_stl_messaging.cpp 
                    ${TREX_CORE_PATH}/src/stx/stl/trex_stl_port.cpp 
                    ${TREX_CORE_PATH}/src/stx/stl/trex_stl_rpc_cmds.cpp 
                    ${TREX_CORE_PATH}/src/stx/stl/trex_stl_stream_vm.cpp 
                    ${TREX_CORE_PATH}/src/stx/stl/trex_stl_stream.cpp 
                    ${TREX_CORE_PATH}/src/stx/stl/trex_stl_streams_compiler.cpp 
                    ${TREX_CORE_PATH}/src/stx/stl/trex_stl_vm_splitter.cpp 
                    ${TREX_CORE_PATH}/src/stx/stl/trex_stl.cpp
                    ${TREX_CORE_PATH}/src/stx/stl/trex_stl_tpg.cpp
                    ${TREX_CORE_PATH}/src/stx/astf/trex_astf_dp_core.cpp 
                    ${TREX_CORE_PATH}/src/stx/astf/trex_astf_messaging.cpp 
                    ${TREX_CORE_PATH}/src/stx/astf/trex_astf_port.cpp 
                    ${TREX_CORE_PATH}/src/stx/astf/trex_astf_rpc_cmds.cpp 
                    ${TREX_CORE_PATH}/src/stx/astf/trex_astf_rx_core.cpp 
                    ${TREX_CORE_PATH}/src/stx/astf/trex_astf_topo.cpp 
                    ${TREX_CORE_PATH}/src/stx/astf/trex_astf.cpp 
                    ${TREX_CORE_PATH}/src/stx/astf/trex_astf_mbuf_redirect.cpp
                    ${TREX_CORE_PATH}/src/stx/astf_batch/trex_astf_batch.cpp)

target_include_directories(trex PRIVATE ${TREX_CORE_PATH}/src
                                        ${TREX_CORE_PATH}/src/drivers
                                        ${TREX_CORE_PATH}/src/publisher
                                        ${TREX_CORE_PATH}/src/utils/
                                        ${TREX_CORE_PATH}/src/stx/common/
                                        ${TREX_CORE_PATH}/src/stx/stf/
                                        ${TREX_CORE_PATH}/src/stx/stl/
                                        ${TREX_CORE_PATH}/src/stx/astf/
                                        ${TREX_CORE_PATH}/src/stx/astf_batch/
                                        ${TREX_CORE_PATH}/src/pal/linux_dpdk/
                                        ${TREX_CORE_PATH}/src/pal/linux_dpdk/dpdk2002_x86_64/
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_cfgfile
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_cryptodev
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_eal
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_ethdev
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_eventdev
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_gro
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_gso
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_hash
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_kni
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_kvargs
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_mbuf
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_mempool
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_meter
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_net
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_pci
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_pdump
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_pipeline
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_port
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_reorder
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_rib
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_ring
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_security
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_timer
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_eal/common/include/
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_eal/linux/eal/include/
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_eal/common/include/arch/x86/
                                        ${TREX_CORE_PATH}/src/dpdk/drivers/net/i40e
                                        ${TREX_CORE_PATH}/src/dpdk/drivers/bus/pci/
                                        ${TREX_CORE_PATH}/src/pal/common/
                                        ${TREX_CORE_PATH}/src/hdrh/
                                        ${TREX_CORE_PATH}/src/stx/
                                        ${TREX_CORE_PATH}/external_libs/json/
                                        ${TREX_CORE_PATH}/external_libs/bpf/
                                        ${TREX_CORE_PATH}/external_libs/zmq/x86_64/include
                                        ${TREX_CORE_PATH}/external_libs/yaml-cpp/include
                                        ${TREX_CORE_PATH}/external_libs/md5/
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_eal/include/
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_eal/x86/include/
                                        ${TREX_CORE_PATH}/src/dpdk/lib/librte_eal/linux/include/
                                        ${TREX_CORE_PATH}/src/dpdk/drivers/net/ntacc/
                                        ${TREX_CORE_PATH}/src/dpdk/drivers)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

set(EXTRA_FLAGS "-g -Wno-format -Wno-deprecated-declarations -Wno-error=uninitialized -march=native -mssse3 -msse4.1 -mpclmul")

set(EXTRA_DEFS WIN_UCODE_SIM _BYTE_ORDER _LITTLE_ENDIAN LINUX RTE_DPDK __STDC_LIMIT_MACROS __STDC_FORMAT_MACROS __STDC_CONSTANT_MACROS 
                RTE_MACHINE_CPUFLAG_SSE RTE_MACHINE_CPUFLAG_SSE2 RTE_MACHINE_CPUFLAG_SSE3 __STDC_FORMAT_MACROS __STDC_CONSTANT_MACROS 
                RTE_MACHINE_CPUFLAG_SSE RTE_MACHINE_CPUFLAG_SSE2 RTE_MACHINE_CPUFLAG_SSE3 
                RTE_MACHINE_CPUFLAG_SSSE3 RTE_MACHINE_CPUFLAG_SSE4_1 RTE_MACHINE_CPUFLAG_SSE4_2 RTE_MACHINE_CPUFLAG_AES 
                RTE_MACHINE_CPUFLAG_PCLMULQDQ RTE_MACHINE_CPUFLAG_AVX 
                RTE_COMPILE_TIME_CPUFLAGS=RTE_CPUFLAG_SSE3,RTE_CPUFLAG_SSE,DRTE_CPUFLAG_SSE2,DRTE_CPUFLAG_SSSE3,RTE_CPUFLAG_SSE4_1,RTE_CPUFLAG_SSE4_2,RTE_CPUFLAG_AES,RTE_CPUFLAG_PCLMULQDQ,RTE_CPUFLAG_AVX 
                TREX_USE_BPFJIT TAP_MAX_QUEUES=16 _GNU_SOURCE PF_DRIVER X722_SUPPORT X722_A0_SUPPORT VF_DRIVER INTEGRATED_VF)

target_compile_definitions(trex PRIVATE ${EXTRA_DEFS})

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -g3 ${EXTRA_FLAGS}")

# set(CMAKE_CXX_FLAGS "${CMAKE_C_FLAGS} -std=c++17 -DWIN_UCODE_SIM -D_BYTE_ORDER -D_LITTLE_ENDIAN -DLINUX -g -Wno-format -Wno-deprecated-declarations -Wno-error=uninitialized")
# set(CMAKE_CXX_FLAGS "${CMAKE_C_FLAGS} -DRTE_DPDK -D__STDC_LIMIT_MACROS -D__STDC_FORMAT_MACROS -D__STDC_CONSTANT_MACROS")
# set(CMAKE_CXX_FLAGS "${CMAKE_C_FLAGS} -march=native -mssse3 -msse4.1 -mpclmul -DRTE_MACHINE_CPUFLAG_SSE -DRTE_MACHINE_CPUFLAG_SSE2 -DRTE_MACHINE_CPUFLAG_SSE3")
# set(CMAKE_CXX_FLAGS "${CMAKE_C_FLAGS} -DRTE_MACHINE_CPUFLAG_SSSE3 -DRTE_MACHINE_CPUFLAG_SSE4_1 -DRTE_MACHINE_CPUFLAG_SSE4_2 -DRTE_MACHINE_CPUFLAG_AES")
# set(CMAKE_CXX_FLAGS "${CMAKE_C_FLAGS} -DRTE_MACHINE_CPUFLAG_PCLMULQDQ -DRTE_MACHINE_CPUFLAG_AVX")
# set(CMAKE_CXX_FLAGS "${CMAKE_C_FLAGS} DRTE_COMPILE_TIME_CPUFLAGS=RTE_CPUFLAG_SSE3,RTE_CPUFLAG_SSE,DRTE_CPUFLAG_SSE2,DRTE_CPUFLAG_SSSE3,RTE_CPUFLAG_SSE4_1,RTE_CPUFLAG_SSE4_2,RTE_CPUFLAG_AES,RTE_CPUFLAG_PCLMULQDQ,RTE_CPUFLAG_AVX")
# set(CMAKE_CXX_FLAGS "${CMAKE_C_FLAGS} -DTREX_USE_BPFJIT -DTAP_MAX_QUEUES=16 -D_GNU_SOURCE -DPF_DRIVER -DX722_SUPPORT -DX722_A0_SUPPORT -DVF_DRIVER -DINTEGRATED_VF")

set(DPDK_LIB_DIRS ${TREX_CORE_PATH}/linux_dpdk ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/linux_dpdk/ ${TREX_CORE_PATH}/external_libs/zmq/x86_64/)

set(DPDK_LINKS ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/44bsd/tcp_output.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/44bsd/tcp_timer.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/44bsd/tcp_debug.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/44bsd/tcp_subr.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/44bsd/flow_table.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/44bsd/tcp_input.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/44bsd/tcp_usrreq.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/44bsd/tcp_socket.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/44bsd/tcp_dpdk.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/44bsd/sch_rampup.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/44bsd/tick_cmd_clock.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/44bsd/udp.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/tunnels/gtp_man.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/hdrh/hdr_time.c.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/hdrh/hdr_encoding.c.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/hdrh/hdr_histogram.c.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/hdrh/hdr_histogram_log.c.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/astf/astf_template_db.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/pal/linux_dpdk/pal_utl.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/pal/linux_dpdk/mbuf.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/pal/common/common_mbuf.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/astf/astf_db.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/astf/astf_json_validator.cpp.8.o  
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/common/basic_utils.cpp.8.o 

${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/common/captureFile.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/common/erf.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/common/pcap.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/common/base64.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/common/n_uniform_prob.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/common/Network/Packet/CPktCmn.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/common/Network/Packet/EthernetHeader.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/common/Network/Packet/IPHeader.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/common/Network/Packet/IPv6Header.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/common/Network/Packet/TCPHeader.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/common/Network/Packet/TCPOptions.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/common/Network/Packet/UDPHeader.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/common/Network/Packet/MacAddress.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/common/Network/Packet/VLANHeader.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/aliasmanager.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/binary.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/contrib/graphbuilder.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/contrib/graphbuilderadapter.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/conversion.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/directives.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/emitfromevents.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/emitter.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/emitterstate.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/emitterutils.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/exp.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/iterator.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/node.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/nodebuilder.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/nodeownership.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/null.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/ostream.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/parser.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/regex.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/scanner.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/scanscalar.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/scantag.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/scantoken.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/simplekey.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/singledocparser.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/stream.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/yaml-cpp/src/tag.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/json/jsoncpp.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/external_libs/md5/md5.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/rpc-server/trex_rpc_server.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/rpc-server/trex_rpc_req_resp_server.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/rpc-server/trex_rpc_jsonrpc_v2_parser.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/rpc-server/trex_rpc_cmds_table.cpp.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/rpc-server/trex_rpc_cmd.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/rpc-server/trex_rpc_zip.cpp.8.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/linux_dpdk/version.c.8.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk_funcs.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/bus/pci/pci_common.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/bus/pci/pci_common_uio.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/bus/pci/pci_params.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/bus/pci/linux/pci.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/bus/pci/linux/pci_uio.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/bus/pci/linux/pci_vfio.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/bus/vdev/vdev.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/bus/vdev/vdev_params.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/bus/vmbus/vmbus_common.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/bus/vmbus/vmbus_channel.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/bus/vmbus/vmbus_bufring.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/bus/vmbus/vmbus_common_uio.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/bus/vmbus/linux/vmbus_bus.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/bus/vmbus/linux/vmbus_uio.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/mempool/ring/rte_mempool_ring.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_cpr.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_ethdev.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_filter.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_flow.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_hwrm.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_irq.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_ring.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_rxq.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_rxr.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_reps.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_stats.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_txq.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_txr.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_util.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_vnic.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/rte_pmd_bnxt.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/bnxt_rxtx_vec_sse.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_core.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/bitalloc.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_msg.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/rand.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/stack.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_em_common.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_em_internal.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_rm.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_tbl.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tfp.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_session.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_device.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_device_p4.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_identifier.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_shadow_tbl.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_shadow_tcam.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_tcam.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_util.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_if_tbl.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/ll.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_global_cfg.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_em_host.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_shadow_identifier.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_core/tf_hash.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/hcapi/hcapi_cfa_p4.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/bnxt_ulp.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_mark_mgr.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_flow_db.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_template_db_tbl.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_template_db_class.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_template_db_act.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_utils.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_mapper.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_matcher.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_rte_parser.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/bnxt_ulp_flow.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_port_db.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_def_rules.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_fc_mgr.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_tun.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_template_db_wh_plus_act.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_template_db_wh_plus_class.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_template_db_stingray_act.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bnxt/tf_ulp/ulp_template_db_stingray_class.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_base.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_80003es2lan.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_82540.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_82541.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_82542.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_82543.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_82571.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_82575.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_api.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_i210.c.4.o
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_ich8lan.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/e1000_logs.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_mac.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_manage.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_mbx.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_nvm.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_osdep.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_phy.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/base/e1000_vf.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/em_ethdev.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/em_rxtx.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/igb_flow.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/igb_ethdev.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/igb_pf.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/e1000/igb_rxtx.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/memif/memif_socket.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/memif/rte_eth_memif.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/virtio/virtio.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/virtio/virtio_ethdev.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/virtio/virtio_pci.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/virtio/virtio_pci_ethdev.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/virtio/virtio_rxtx.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/virtio/virtio_rxtx_simple.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/virtio/virtqueue.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/virtio/virtio_user_ethdev.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/virtio/virtio_user/vhost_vdpa.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/virtio/virtio_user/vhost_kernel.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/virtio/virtio_user/vhost_kernel_tap.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/virtio/virtio_user/vhost_user.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/virtio/virtio_user/virtio_user_dev.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/common/iavf/iavf_adminq.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/common/iavf/iavf_common.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/common/iavf/iavf_impl.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_rcu/rte_rcu_qsbr.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_cfgfile/rte_cfgfile.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_hypervisor.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_dynmem.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_bus.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_class.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_cpuflags.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_debug.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_dev.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_devargs.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_errno.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_fbarray.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_hexdump.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_launch.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_lcore.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_log.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_memalloc.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_memory.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_memzone.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_mcfg.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_options.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_proc.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_string_fns.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_tailqs.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_thread.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_timer.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_config.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_trace.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_trace_ctf.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_trace_points.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_trace_utils.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/eal_common_uuid.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/rte_reciprocal.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/hotplug_mp.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/malloc_elem.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/malloc_heap.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/malloc_mp.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/rte_keepalive.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/rte_malloc.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/rte_service.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/common/rte_random.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/unix/eal_unix_timer.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/unix/eal_unix_memory.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/unix/eal_file.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/unix/rte_thread.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/linux/eal.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/linux/eal_alarm.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/linux/eal_cpuflags.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/linux/eal_debug.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/linux/eal_hugepage_info.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/linux/eal_interrupts.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/linux/eal_lcore.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/linux/eal_log.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/linux/eal_memalloc.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/linux/eal_memory.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/linux/eal_thread.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/linux/eal_timer.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/linux/eal_vfio_mp_sync.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/linux/eal_vfio.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/linux/eal_dev.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_ethdev/rte_ethdev.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_ethdev/rte_flow.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_ethdev/ethdev_trace_points.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_ethdev/ethdev_private.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_ethdev/rte_class_eth.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_ethdev/ethdev_profile.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_ethdev/rte_mtr.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_ethdev/rte_tm.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_telemetry/telemetry.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_telemetry/telemetry_data.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_telemetry/telemetry_legacy.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_hash/rte_cuckoo_hash.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_kvargs/rte_kvargs.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_mbuf/rte_mbuf.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_mbuf/rte_mbuf_dyn.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_mbuf/rte_mbuf_ptype.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_mbuf/rte_mbuf_pool_ops.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_mempool/rte_mempool.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_mempool/rte_mempool_ops.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_mempool/rte_mempool_ops_default.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_mempool/mempool_trace_points.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_net/rte_ether.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_net/rte_net.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_net/rte_net_crc.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_net/rte_arp.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_pci/rte_pci.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_ring/rte_ring.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_timer/rte_timer.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_gso/rte_gso.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_gso/gso_tunnel_udp4.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_gso/gso_common.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_gso/gso_tcp4.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_gso/gso_tunnel_tcp4.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_gso/gso_udp4.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/base/i40e_adminq.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/base/i40e_common.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/base/i40e_dcb.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/base/i40e_diag.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/base/i40e_hmc.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/base/i40e_lan_hmc.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/base/i40e_nvm.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/i40e_hash.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/i40e_ethdev.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/i40e_ethdev_vf.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/i40e_fdir.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/i40e_flow.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/i40e_pf.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/i40e_rxtx.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/i40e_tm.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/i40e_vf_representor.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/rte_pmd_i40e.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/enic/enic_ethdev.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/enic/base/vnic_intr.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/enic/base/vnic_rq.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/enic/base/vnic_wq.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/enic/base/vnic_dev.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/enic/base/vnic_cq.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/enic/enic_vf_representor.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/enic/enic_flow.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/enic/enic_fm_flow.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/enic/enic_rxtx.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/enic/enic_res.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/enic/enic_main.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/base/ice_vlan_mode.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/base/ice_acl.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/base/ice_acl_ctrl.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/base/ice_controlq.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/base/ice_common.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/base/ice_sched.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/base/ice_switch.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/base/ice_nvm.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/base/ice_flex_pipe.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/base/ice_flow.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/base/ice_dcb.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/base/ice_fdir.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/ice_dcf_vf_representor.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/ice_acl_filter.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/ice_dcf.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/ice_dcf_ethdev.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/ice_dcf_parent.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/ice_ethdev.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/ice_rxtx.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/ice_rxtx_vec_sse.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/ice_switch_filter.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/ice_fdir_filter.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/ice_hash.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ice/ice_generic_flow.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/base/ixgbe_82598.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/base/ixgbe_82599.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/base/ixgbe_api.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/base/ixgbe_common.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/base/ixgbe_dcb.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/base/ixgbe_dcb_82598.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/base/ixgbe_dcb_82599.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/base/ixgbe_hv_vf.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/base/ixgbe_mbx.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/base/ixgbe_phy.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/base/ixgbe_vf.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/base/ixgbe_x540.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/base/ixgbe_x550.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/ixgbe_ethdev.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/ixgbe_fdir.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/ixgbe_flow.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/ixgbe_pf.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/ixgbe_rxtx.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/ixgbe_rxtx_vec_sse.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/ixgbe_tm.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/ixgbe_vf_representor.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ixgbe/rte_pmd_ixgbe.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/i40e/i40e_rxtx_vec_sse.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/virtio/virtio_rxtx_simple_sse.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/vmxnet3/vmxnet3_ethdev.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/vmxnet3/vmxnet3_rxtx.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/af_packet/rte_eth_af_packet.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ena/ena_ethdev.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ena/base/ena_com.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/ena/base/ena_eth_com.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/x86/rte_cpuflags.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/x86/rte_spinlock.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/x86/rte_cycles.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_eal/x86/rte_hypervisor.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/failsafe/failsafe.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/failsafe/failsafe_args.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/failsafe/failsafe_eal.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/failsafe/failsafe_ops.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/failsafe/failsafe_rxtx.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/failsafe/failsafe_ether.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/failsafe/failsafe_flow.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/failsafe/failsafe_intr.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/vdev_netvsc/vdev_netvsc.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/netvsc/hn_ethdev.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/netvsc/hn_rxtx.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/netvsc/hn_rndis.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/netvsc/hn_nvs.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/netvsc/hn_vf.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_ip_frag/rte_ipv4_fragmentation.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_ip_frag/rte_ipv6_fragmentation.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_ip_frag/rte_ipv4_reassembly.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_ip_frag/rte_ipv6_reassembly.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_ip_frag/rte_ip_frag_common.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/lib/librte_ip_frag/ip_frag_internal.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bonding/rte_eth_bond_api.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bonding/rte_eth_bond_pmd.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bonding/rte_eth_bond_flow.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bonding/rte_eth_bond_args.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bonding/rte_eth_bond_8023ad.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/dpdk/drivers/net/bonding/rte_eth_bond_alb.c.4.o 
${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/drivers/trex_ixgbe_fdir.c.4.o ${TREX_CORE_PATH}/linux_dpdk/build_dpdk/src/drivers/trex_i40e_fdir.c.4.o)

set(EXTRA_LINKS -Wl,-rpath,so -Wl,-rpath,so/x86_64 -Wl,-Bstatic -Wl,-Bdynamic bpf-64-debug zmq pthread dl z)

target_link_directories(trex PRIVATE ${DPDK_LIB_DIRS})
target_link_libraries(trex ${EXTRA_LINKS})
target_link_options(trex PRIVATE ${DPDK_LINKS})
# target_link_options(trex ${DPDK_LINKS})