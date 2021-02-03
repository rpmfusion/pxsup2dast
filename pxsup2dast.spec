Name:           pxsup2dast
Version:        20120704
Release:        14%{?dist}
Summary:        Project X to dvdauthor subtitle converter

License:        GPLv2
URL:            http://www.guru-group.fi/~too/sw/m2vmp2cut/
Source0:        http://www.guru-group.fi/~too/sw/m2vmp2cut/pxsup2dast.c

BuildRequires:  perl
BuildRequires:  zlib-devel

%description
pxsup2dast converts Project X's sup subtitles to XML subtitle files
for use with dvdauthor.


%prep
%setup -c -T
perl -pe 's/-O2/\$RPM_OPT_FLAGS \$RPM_LD_FLAGS/' %{SOURCE0} > %{name}.c


%build
sh %{name}.c


%install
install -Dpm 755 pxsup2dast $RPM_BUILD_ROOT%{_bindir}/pxsup2dast


%files
%{_bindir}/pxsup2dast


%changelog
* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20120704-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20120704-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20120704-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20120704-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20120704-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 20120704-9
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20120704-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 20120704-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 20120704-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 20120704-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 20120704-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue May 14 2013 Martin Gansser <martinkg@fedoraproject.org> - 20120704-3
- rebuild with recent source file

* Mon May 13 2013 Martin Gansser <martinkg@fedoraproject.org> - 20120704-2
- rebuild

* Thu Jul 4 2012 Ville Skyttä <ville.skytta@iki.fi> - 20120704-1
- Update to 20120704.

* Sun Aug 29 2010 Ville Skyttä <ville.skytta@iki.fi> - 20100827-1
- Update to 20100827.

* Sun Jan 10 2010 Ville Skyttä <ville.skytta@iki.fi> - 20090809-1
- Update to 20090809, POSIX 2008 build fix applied upstream.

* Tue Aug  4 2009 Ville Skyttä <ville.skytta@iki.fi> - 20090111-2
- Fix POSIX 2008 build.

* Thu Feb  5 2009 Ville Skyttä <ville.skytta@iki.fi> - 20090111-1
- 2009-01-11.

* Fri May 25 2007 Ville Skyttä <ville.skytta@iki.fi> - 20070305-1
- 2007-03-05.

* Sat Sep 30 2006 Ville Skyttä <ville.skytta@iki.fi> - 20060125-2
- Rebuild.

* Thu Aug 17 2006 Ville Skyttä <ville.skytta@iki.fi> - 20060125-1
- First build.

