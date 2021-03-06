#--------------------------------------------------------------------
# Inviwo fermi Module
ivw_module(Fermi)

#--------------------------------------------------------------------
# Add header files
set(HEADER_FILES
    fermimodule.h
    fermimoduledefine.h
)
ivw_group("Header Files" ${HEADER_FILES})

#--------------------------------------------------------------------
# Add source files
set(SOURCE_FILES
    fermimodule.cpp
)
ivw_group("Source Files" ${SOURCE_FILES})


#--------------------------------------------------------------------
# Add shaders
set(SHADER_FILES
    #${CMAKE_CURRENT_SOURCE_DIR}/glsl/fermiprocessor.frag
)
ivw_group("Shader Files" ${SHADER_FILES})


#--------------------------------------------------------------------
# Add Unittests
set(TEST_FILES
    tests/unittests/fermi-unittest-main.cpp
    tests/unittests/scripts-test.cpp
    tests/unittests/scripts/brillouin_zone.py
    tests/unittests/scripts/expand_zone.py
)
ivw_add_unittest(${TEST_FILES})

#--------------------------------------------------------------------
# Create module
ivw_create_module(${SOURCE_FILES} ${HEADER_FILES} ${SHADER_FILES})

#--------------------------------------------------------------------
# Add shader directory to pack
# ivw_add_to_module_pack(${CMAKE_CURRENT_SOURCE_DIR}/glsl)
