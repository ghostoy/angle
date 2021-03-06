# Copyright (c) 2014 The ANGLE Project Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
    'variables':
    {
        'util_sources':
        [
            'com_utils.h',
            'keyboard.h',
            'mouse.h',
            'path_utils.h',
            'random_utils.cpp',
            'random_utils.h',
            'shader_utils.cpp',
            'shader_utils.h',
            'EGLWindow.cpp',
            'EGLWindow.h',
            'Event.h',
            'OSWindow.cpp',
            'OSWindow.h',
            'Timer.h',
        ],
        'util_win32_sources':
        [
            'win32/Win32_path_utils.cpp',
            'win32/Win32Timer.cpp',
            'win32/Win32Timer.h',
            'win32/Win32Window.cpp',
            'win32/Win32Window.h',
        ],
        'util_linux_sources':
        [
            'linux/Linux_path_utils.cpp',
            'linux/LinuxTimer.cpp',
            'linux/LinuxTimer.h',
            'x11/X11Window.cpp',
            'x11/X11Window.h',
        ]
    },
    'targets':
    [
        {
            'target_name': 'angle_util',
            'type': 'static_library',
            'includes': [ '../build/common_defines.gypi', ],
            'dependencies':
            [
                '<(angle_path)/src/angle.gyp:angle_common',
                '<(angle_path)/src/angle.gyp:libEGL',
                '<(angle_path)/src/angle.gyp:libGLESv2',
            ],
            'export_dependent_settings':
            [
                '<(angle_path)/src/angle.gyp:angle_common',
            ],
            'include_dirs':
            [
                '<(angle_path)/include',
                '<(angle_path)/util',
            ],
            'sources':
            [
                '<@(util_sources)',
            ],
            'direct_dependent_settings':
            {
                'include_dirs':
                [
                    '<(angle_path)/include',
                    '<(angle_path)/util',
                ],
            },
            'conditions':
            [
                ['OS=="win"',
                {
                    'msvs_disabled_warnings': [ 4201 ],
                    'sources':
                    [
                        '<@(util_win32_sources)',
                    ],
                }],
                ['OS=="linux"',
                {
                    'sources':
                    [
                        '<@(util_linux_sources)',
                    ],
                    'link_settings': {
                        'ldflags': [
                            '<!@(pkg-config --libs-only-L --libs-only-other x11 xi)',
                        ],
                        'libraries': [
                            '<!@(pkg-config --libs-only-l x11 xi) -lrt',
                        ],
                    },
                }],
            ],
        },
    ],
}
