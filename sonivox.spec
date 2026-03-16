%define		major 4
%define		libname %mklibname %{name}
%define		develname %mklibname %{name} -d

Summary:		Fork of the AOSP 'platform_external_sonivox' project
Name:	sonivox
Version:		4.0.1
Release:		1
License:		ASL 2.0
Group:	Sound
Url:		https://github.com/pedrolcl/sonivox
Source0:	https://github.com/pedrolcl/sonivox/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:		cmake >= 3.21
BuildRequires:		make
BuildRequires:		pkgconfig(zlib)
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

%files
%{_bindir}/sonivoxrender

#-----------------------------------------------------------------------------

%package	-n %{libname}
Summary:		Fork of the AOSP 'platform_external_sonivox' project
Group:	System/Libraries

%description -n %{libname}
Sonivox is a fork of the Android Open Source Project 'platform_external_sonivox'
including a CMake based build system to be used not on Android, but on any other
Operating System.
This package contains the main library for %{name}.

%files -n %{libname}
%license LICENSE
%{_libdir}/lib%{name}.so.%{major}{,.*}

#-----------------------------------------------------------------------------

%package -n     %{develname}
Summary:		Development package for %{name}
Group:	Development/C++
Requires:	%{name} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Header files for development with %{name}.

%files -n %{develname}
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man1/sonivoxrender.1.*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake \
       -DBUILD_TESTING:BOOL=FALSE \
       -DBUILD_MANPAGE:BOOL=FALSE

%make_build


%install
%make_install -C build
