# Copyright 2015 The ANGLE Project Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# angle_perftests.gypi:
#
# This .gypi describes all of the sources and dependencies to build a
# unified "angle_perftests" target, which contains all of ANGLE's
# performance tests (buffer updates, texture updates, draw calls, etc)
# It requires a parent target to include this gypi in an executable
# target containing a gtest harness in a main.cpp.

{
    'variables':
    {
        'angle_perf_tests_sources':
        [
            'perf_tests/ANGLEPerfTest.cpp',
            'perf_tests/ANGLEPerfTest.h',
            'perf_tests/BufferSubData.cpp',
            'perf_tests/DrawCallPerf.cpp',
            'perf_tests/IndexConversionPerf.cpp',
            'perf_tests/PointSprites.cpp',
            'perf_tests/TexSubImage.cpp',
            'perf_tests/third_party/perf/perf_test.cc',
            'perf_tests/third_party/perf/perf_test.h',
            'test_utils/angle_test_instantiate.h',
        ],
        'angle_perf_tests_win_sources':
        [
            'perf_tests/IndexDataManagerTest.cpp',
        ]
    },
    'dependencies':
    [
        '<(angle_path)/src/angle.gyp:angle_common',
        '<(angle_path)/src/angle.gyp:libANGLE', # for unit testing
        '<(angle_path)/src/angle.gyp:libGLESv2',
        '<(angle_path)/src/angle.gyp:libEGL',
        '<(angle_path)/src/tests/tests.gyp:angle_test_support',
        '<(angle_path)/util/util.gyp:angle_util',
    ],
    'include_dirs':
    [
        '<(angle_path)/include',
    ],
    'sources':
    [
        '<@(angle_perf_tests_sources)',
    ],
    'include_dirs':
    [
        '<(angle_path)/src/tests'
    ],
    'conditions':
    [
        ['OS=="win"',
        {
            'sources':
            [
                '<@(angle_perf_tests_win_sources)',
            ],
        }],
    ]
}
