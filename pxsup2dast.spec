Name:           pxsup2dast
Version:        20120704
Release:        4%{?dist}
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

