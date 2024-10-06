%define major     3
%define libname   %mklibname %{name}
%define develname %mklibname %{name} -d

Name:           sonivox
Version:        3.6.14
Release:        1
Summary:        Fork of the AOSP 'platform_external_sonivox' project
Group:          System/Libraries
License:        ASL 2.0
URL:            https://github.com/pedrolcl/sonivox
Source:         https://github.com/pedrolcl/sonivox/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake

Requires:       %{libname} = %{version}-%{release}

%description
Sonivox is a fork of the Android Open Source Project 'platform_external_sonivox'
including a CMake based build system to be used not on Android, but on any other
Operating System.

This is a Wave Table synthesizer, not using external soundfont files but
embedded samples instead. It is also a real time GM synthesizer.
It may be indicated in projects for small embedded devices. There is neither
MIDI input nor Audio output facilities included in the library. You need to
provide your own input/output.


%package -n     %{libname}
Summary:        Fork of the AOSP 'platform_external_sonivox' project
Group:          System/Libraries

%description -n %{libname}
Sonivox is a fork of the Android Open Source Project 'platform_external_sonivox'
including a CMake based build system to be used not on Android, but on any other
Operating System.

This is a Wave Table synthesizer, not using external soundfont files but
embedded samples instead. It is also a real time GM synthesizer.
It may be indicated in projects for small embedded devices. There is neither
MIDI input nor Audio output facilities included in the library. You need to
provide your own input/output.

%package -n     %{develname}
Summary:        Development package for %{name}
Group:          Development/C++
Requires:       %{name} = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
Header files for development with %{name}.

%prep
%autosetup -p1

%build
%cmake \
       -DBUILD_TESTING:BOOL=FALSE \
       -DBUILD_SONIVOX_STATIC:BOOL=FALSE

%make_build

%install
%make_install -C build

%files
%{_bindir}/sonivoxrender

%files -n %{libname}
%license LICENSE
%{_libdir}/lib%{name}.so.%{major}{,.*}

%files -n %{develname}
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man1/sonivoxrender.1.*
