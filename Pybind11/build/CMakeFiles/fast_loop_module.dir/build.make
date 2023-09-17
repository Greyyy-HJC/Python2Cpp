# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.23

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/homebrew/Cellar/cmake/3.23.2/bin/cmake

# The command to remove a file.
RM = /opt/homebrew/Cellar/cmake/3.23.2/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/greyyy/git/Python2Cpp/Pybind11

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/greyyy/git/Python2Cpp/Pybind11/build

# Include any dependencies generated for this target.
include CMakeFiles/fast_loop_module.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/fast_loop_module.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/fast_loop_module.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/fast_loop_module.dir/flags.make

CMakeFiles/fast_loop_module.dir/fast_loop.cpp.o: CMakeFiles/fast_loop_module.dir/flags.make
CMakeFiles/fast_loop_module.dir/fast_loop.cpp.o: ../fast_loop.cpp
CMakeFiles/fast_loop_module.dir/fast_loop.cpp.o: CMakeFiles/fast_loop_module.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/greyyy/git/Python2Cpp/Pybind11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/fast_loop_module.dir/fast_loop.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/fast_loop_module.dir/fast_loop.cpp.o -MF CMakeFiles/fast_loop_module.dir/fast_loop.cpp.o.d -o CMakeFiles/fast_loop_module.dir/fast_loop.cpp.o -c /Users/greyyy/git/Python2Cpp/Pybind11/fast_loop.cpp

CMakeFiles/fast_loop_module.dir/fast_loop.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/fast_loop_module.dir/fast_loop.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/greyyy/git/Python2Cpp/Pybind11/fast_loop.cpp > CMakeFiles/fast_loop_module.dir/fast_loop.cpp.i

CMakeFiles/fast_loop_module.dir/fast_loop.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/fast_loop_module.dir/fast_loop.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/greyyy/git/Python2Cpp/Pybind11/fast_loop.cpp -o CMakeFiles/fast_loop_module.dir/fast_loop.cpp.s

# Object files for target fast_loop_module
fast_loop_module_OBJECTS = \
"CMakeFiles/fast_loop_module.dir/fast_loop.cpp.o"

# External object files for target fast_loop_module
fast_loop_module_EXTERNAL_OBJECTS =

libfast_loop_module.so: CMakeFiles/fast_loop_module.dir/fast_loop.cpp.o
libfast_loop_module.so: CMakeFiles/fast_loop_module.dir/build.make
libfast_loop_module.so: /opt/homebrew/opt/fftw/lib/libfftw3.a
libfast_loop_module.so: CMakeFiles/fast_loop_module.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/greyyy/git/Python2Cpp/Pybind11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared module libfast_loop_module.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/fast_loop_module.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/fast_loop_module.dir/build: libfast_loop_module.so
.PHONY : CMakeFiles/fast_loop_module.dir/build

CMakeFiles/fast_loop_module.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/fast_loop_module.dir/cmake_clean.cmake
.PHONY : CMakeFiles/fast_loop_module.dir/clean

CMakeFiles/fast_loop_module.dir/depend:
	cd /Users/greyyy/git/Python2Cpp/Pybind11/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/greyyy/git/Python2Cpp/Pybind11 /Users/greyyy/git/Python2Cpp/Pybind11 /Users/greyyy/git/Python2Cpp/Pybind11/build /Users/greyyy/git/Python2Cpp/Pybind11/build /Users/greyyy/git/Python2Cpp/Pybind11/build/CMakeFiles/fast_loop_module.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/fast_loop_module.dir/depend
