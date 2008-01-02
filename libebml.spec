%define name    libebml
%define version 0.7.7
%define libname %mklibname ebml 0
%define rel 1
#fixed2
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}

Summary:        Extensible Binary Meta Language Library
Name:           %name
Version:        %version
Release: %mkrel %rel
License:        GPL/QPL
Group:		System/Libraries
URL:            http://www.matroska.org/
Source0:        http://dl.matroska.org/downloads/libebml/%name-%version.tar.bz2
BuildRoot:      %_tmppath/%name-buildroot
%description
This library is used for I/O operations in the Extensible Binary Meta
Language (EBML), which is a kind of binary version of XML.

%package -n %libname
Summary:        Extensible Binary Meta Language shared Library
Group: System/Libraries

%description -n %libname
This library is used for I/O operations in the Extensible Binary Meta
Language (EBML), which is a kind of binary version of XML.

%package -n %libname-devel
Group: Development/C++
Summary: Extensible Binary Meta Language Library headers and static library
Obsoletes: libebml-devel
Provides: libebml-devel = %version
Requires: %libname = %version

%description -n %libname-devel
This library is used for I/O operations in the Extensible Binary Meta
Language (EBML), which is a kind of binary version of XML.

This package contains the C++ headers and the static library needed
for development with EBML.

%prep
%setup -q

%build
cd make/linux
%make


%install
rm -rf %buildroot
cd make/linux
%makeinstall_std prefix=%buildroot/%_prefix libdir=%buildroot/%_libdir

%clean
rm -rf %buildroot

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%_libdir/lib*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%doc LICENSE*
#%doc src/api/index.html
%{_includedir}/ebml
%{_libdir}/libebml.a
%{_libdir}/libebml.so


