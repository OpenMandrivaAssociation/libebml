%define major 3
%define libname %mklibname ebml %{major}
%define develname %mklibname ebml -d

Summary:	Extensible Binary Meta Language Library
Name:		libebml
Version:	1.2.2
Release:	2
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.matroska.org/
Source0:	http://dl.matroska.org/downloads/libebml/%{name}-%{version}.tar.bz2

%description
This library is used for I/O operations in the Extensible Binary Meta
Language (EBML), which is a kind of binary version of XML.

%package -n %{libname}
Summary:	Extensible Binary Meta Language shared Library
Group:		System/Libraries

%description -n %{libname}
This library is used for I/O operations in the Extensible Binary Meta
Language (EBML), which is a kind of binary version of XML.

%package -n %{develname}
Group:		Development/C++
Summary:	Extensible Binary Meta Language Library headers and static library
Provides:	libebml-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
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
cd make/linux
%makeinstall_std prefix=%{buildroot}%{_prefix} libdir=%{buildroot}%{_libdir}

# To avoid unstripped-binary-or-object
chmod 0755 %{buildroot}%{_libdir}/lib*.so.%{major}*

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc LICENSE*
%{_includedir}/ebml
%{_libdir}/libebml.a
%{_libdir}/libebml.so




%changelog
* Fri Sep 23 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.2-1mdv2012.0
+ Revision: 701136
- update to new version 1.2.2

* Sun Jun 26 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.1-1
+ Revision: 687333
- update to new version 1.2.1

* Sun Jan 30 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.0-1
+ Revision: 634154
- new version
- new major 3

* Sat Jul 10 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 550264
- new version
- new major

* Tue Aug 26 2008 Emmanuel Andry <eandry@mandriva.org> 0.7.8-3mdv2009.0
+ Revision: 276359
- apply devel policy
- fix license
- check major

* Fri Jul 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.8-2mdv2009.0
+ Revision: 233729
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 05 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.8-1mdv2008.1
+ Revision: 180077
- new version

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.7.7-1mdv2008.1
+ Revision: 140921
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.7-1mdv2007.0
+ Revision: 108690
- Import libebml

* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 0.7.7-1mdv2007.1
- rebuild

* Mon Apr 03 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.7-1mdk
- New release 0.7.7

* Wed Oct 19 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.6-1mdk
- New release 0.7.6

* Thu Jun 09 2005 Götz Waschk <waschk@mandriva.org> 0.7.5-2mdk
- mkrel

* Tue May 24 2005 Götz Waschk <waschk@mandriva.org> 0.7.5-1mdk
- New release 0.7.5

* Tue Apr 19 2005 Götz Waschk <waschk@linux-mandrake.com> 0.7.4-1mdk
- libify
- New release 0.7.4

* Mon Feb 07 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.7.3-1mdk
- 0.7.3

* Tue Nov 09 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.2-1mdk
- New release 0.7.2

* Mon Jul 26 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.1-1mdk
- fix source URL
- New release 0.7.1

* Tue Jun 08 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.0-2mdk
- rebuild for new g++

* Sat Apr 24 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.0-1mdk
- new version

* Sat Apr 03 2004 Götz Waschk <waschk@linux-mandrake.com> 0.6.5-1mdk
- new version

* Thu Jan 22 2004 Götz Waschk <waschk@linux-mandrake.com> 0.6.4-1mdk
- new version

