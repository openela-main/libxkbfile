Summary: X.Org X11 libxkbfile runtime library
Name: libxkbfile
Version: 1.1.0
Release: 8%{?dist}
License: MIT
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: pkgconfig(xproto) pkgconfig(x11)
BuildRequires: gcc

%description
X.Org X11 libxkbfile runtime library

%package devel
Summary: X.Org X11 libxkbfile development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libxkbfile development package

%prep
%setup -q

%build
# FIXME: We use -fno-strict-aliasing, to work around the following bug:
# maprules.c:1373: warning: dereferencing type-punned pointer will break strict-aliasing rules)
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING ChangeLog
%{_libdir}/libxkbfile.so.1
%{_libdir}/libxkbfile.so.1.0.2

%files devel
%{_includedir}/X11/extensions/XKBbells.h
%{_includedir}/X11/extensions/XKBconfig.h
%{_includedir}/X11/extensions/XKBfile.h
%{_includedir}/X11/extensions/XKBrules.h
%{_includedir}/X11/extensions/XKM.h
%{_includedir}/X11/extensions/XKMformat.h
%{_libdir}/libxkbfile.so
%{_libdir}/pkgconfig/xkbfile.pc

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.1.0-8
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.1.0-7
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 12:14:47 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.0-5
- Add BuildRequires for make

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Adam Jackson <ajax@redhat.com> - 1.1.0-1
- libxkbfile 1.1.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Benjamin Tissoires <benjamin.tissoires@redhat.com> 1.0.9-11
- Add buildrequires gcc (#1604693 because of #1551327)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Adam Jackson <ajax@redhat.com> - 1.0.9-9
- Drop useless %%defattr

* Fri Jun 29 2018 Adam Jackson <ajax@redhat.com> - 1.0.9-8
- Use ldconfig scriptlet macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 07 2017 Benjamin Tissoires <benjamin.tissoires@redhat.com>
- Fixed changelog entry

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Adam Jackson <ajax@redhat.com> 1.0.9-1
- libxkbfile 1.0.9
