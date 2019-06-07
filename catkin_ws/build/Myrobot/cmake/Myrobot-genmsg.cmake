# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "Myrobot: 1 messages, 1 services")

set(MSG_I_FLAGS "-IMyrobot:/home/zmx/catkin_ws/src/Myrobot/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(Myrobot_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/zmx/catkin_ws/src/Myrobot/srv/AddTwoInts.srv" NAME_WE)
add_custom_target(_Myrobot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "Myrobot" "/home/zmx/catkin_ws/src/Myrobot/srv/AddTwoInts.srv" ""
)

get_filename_component(_filename "/home/zmx/catkin_ws/src/Myrobot/msg/Num.msg" NAME_WE)
add_custom_target(_Myrobot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "Myrobot" "/home/zmx/catkin_ws/src/Myrobot/msg/Num.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(Myrobot
  "/home/zmx/catkin_ws/src/Myrobot/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/Myrobot
)

### Generating Services
_generate_srv_cpp(Myrobot
  "/home/zmx/catkin_ws/src/Myrobot/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/Myrobot
)

### Generating Module File
_generate_module_cpp(Myrobot
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/Myrobot
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(Myrobot_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(Myrobot_generate_messages Myrobot_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/zmx/catkin_ws/src/Myrobot/srv/AddTwoInts.srv" NAME_WE)
add_dependencies(Myrobot_generate_messages_cpp _Myrobot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/zmx/catkin_ws/src/Myrobot/msg/Num.msg" NAME_WE)
add_dependencies(Myrobot_generate_messages_cpp _Myrobot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(Myrobot_gencpp)
add_dependencies(Myrobot_gencpp Myrobot_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS Myrobot_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(Myrobot
  "/home/zmx/catkin_ws/src/Myrobot/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/Myrobot
)

### Generating Services
_generate_srv_eus(Myrobot
  "/home/zmx/catkin_ws/src/Myrobot/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/Myrobot
)

### Generating Module File
_generate_module_eus(Myrobot
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/Myrobot
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(Myrobot_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(Myrobot_generate_messages Myrobot_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/zmx/catkin_ws/src/Myrobot/srv/AddTwoInts.srv" NAME_WE)
add_dependencies(Myrobot_generate_messages_eus _Myrobot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/zmx/catkin_ws/src/Myrobot/msg/Num.msg" NAME_WE)
add_dependencies(Myrobot_generate_messages_eus _Myrobot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(Myrobot_geneus)
add_dependencies(Myrobot_geneus Myrobot_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS Myrobot_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(Myrobot
  "/home/zmx/catkin_ws/src/Myrobot/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/Myrobot
)

### Generating Services
_generate_srv_lisp(Myrobot
  "/home/zmx/catkin_ws/src/Myrobot/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/Myrobot
)

### Generating Module File
_generate_module_lisp(Myrobot
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/Myrobot
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(Myrobot_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(Myrobot_generate_messages Myrobot_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/zmx/catkin_ws/src/Myrobot/srv/AddTwoInts.srv" NAME_WE)
add_dependencies(Myrobot_generate_messages_lisp _Myrobot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/zmx/catkin_ws/src/Myrobot/msg/Num.msg" NAME_WE)
add_dependencies(Myrobot_generate_messages_lisp _Myrobot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(Myrobot_genlisp)
add_dependencies(Myrobot_genlisp Myrobot_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS Myrobot_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(Myrobot
  "/home/zmx/catkin_ws/src/Myrobot/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/Myrobot
)

### Generating Services
_generate_srv_nodejs(Myrobot
  "/home/zmx/catkin_ws/src/Myrobot/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/Myrobot
)

### Generating Module File
_generate_module_nodejs(Myrobot
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/Myrobot
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(Myrobot_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(Myrobot_generate_messages Myrobot_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/zmx/catkin_ws/src/Myrobot/srv/AddTwoInts.srv" NAME_WE)
add_dependencies(Myrobot_generate_messages_nodejs _Myrobot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/zmx/catkin_ws/src/Myrobot/msg/Num.msg" NAME_WE)
add_dependencies(Myrobot_generate_messages_nodejs _Myrobot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(Myrobot_gennodejs)
add_dependencies(Myrobot_gennodejs Myrobot_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS Myrobot_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(Myrobot
  "/home/zmx/catkin_ws/src/Myrobot/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/Myrobot
)

### Generating Services
_generate_srv_py(Myrobot
  "/home/zmx/catkin_ws/src/Myrobot/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/Myrobot
)

### Generating Module File
_generate_module_py(Myrobot
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/Myrobot
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(Myrobot_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(Myrobot_generate_messages Myrobot_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/zmx/catkin_ws/src/Myrobot/srv/AddTwoInts.srv" NAME_WE)
add_dependencies(Myrobot_generate_messages_py _Myrobot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/zmx/catkin_ws/src/Myrobot/msg/Num.msg" NAME_WE)
add_dependencies(Myrobot_generate_messages_py _Myrobot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(Myrobot_genpy)
add_dependencies(Myrobot_genpy Myrobot_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS Myrobot_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/Myrobot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/Myrobot
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(Myrobot_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/Myrobot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/Myrobot
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(Myrobot_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/Myrobot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/Myrobot
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(Myrobot_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/Myrobot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/Myrobot
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(Myrobot_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/Myrobot)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/Myrobot\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/Myrobot
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(Myrobot_generate_messages_py std_msgs_generate_messages_py)
endif()
