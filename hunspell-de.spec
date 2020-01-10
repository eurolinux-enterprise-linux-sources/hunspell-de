Name: hunspell-de
Summary: German hunspell dictionaries
%define upstreamid 20120607
Version: 0.%{upstreamid}
Release: 3%{?dist}
Source: http://www.j3e.de/ispell/igerman98/dict/igerman98-%{upstreamid}.tar.bz2
Group: Applications/Text
URL: http://www.j3e.de/ispell/igerman98
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2 or GPLv3
BuildArch: noarch
BuildRequires: aspell, hunspell

Requires: hunspell

%description
German (Germany, Switzerland, etc.) hunspell dictionaries.

%prep
%setup -q -n igerman98-%{upstreamid}
sed -i -e "s/AFFIX_EXPANDER = ispell/AFFIX_EXPANDER = aspell/g" Makefile

%build
make hunspell/de_AT.dic hunspell/de_AT.aff \
     hunspell/de_CH.dic hunspell/de_CH.aff \
     hunspell/de_DE.dic hunspell/de_DE.aff
cd hunspell
for i in README_*.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cd hunspell
cp -p de_??.dic de_??.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
de_DE_aliases="de_BE de_LU"
for lang in $de_DE_aliases; do
	ln -s de_DE.aff $lang.aff
	ln -s de_DE.dic $lang.dic
done
de_CH_aliases="de_LI"
for lang in $de_CH_aliases; do
	ln -s de_CH.aff $lang.aff
	ln -s de_CH.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc hunspell/README_de_??.txt hunspell/COPYING_OASIS hunspell/COPYING_GPLv2 hunspell/COPYING_GPLv3 hunspell/Copyright
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20120607-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20120607-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 13 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120607-1
- latest version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110609-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 09 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110609-1
- latest version

* Mon Mar 21 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110321-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100727-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 30 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100727-1
- latest version

* Thu Oct 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20091006-1
- latest version
- drop integrated igerman98-20090107-useaspell.patch

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090107-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090107-3
- tidy spec

* Thu Apr 23 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090107-2
- fix dictionaries

* Thu Feb 26 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090107-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20071211-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 11 2007 Caolán McNamara <caolanm@redhat.com> - 0.20071211-1
- latest version

* Thu Aug 30 2007 Caolán McNamara <caolanm@redhat.com> - 0.20070829-1
- latest version
- build from canonical source

* Fri Aug 03 2007 Caolán McNamara <caolanm@redhat.com> - 0.20051213-2
- clarify license version

* Thu Dec 07 2006 Caolán McNamara <caolanm@redhat.com> - 0.20051213-1
- initial version
