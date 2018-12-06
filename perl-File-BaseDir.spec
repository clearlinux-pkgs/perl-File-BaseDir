#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-BaseDir
Version  : 0.08
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/K/KI/KIMRYAN/File-BaseDir-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KI/KIMRYAN/File-BaseDir-0.08.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-basedir-perl/libfile-basedir-perl_0.08-1.debian.tar.xz
Summary  : 'Use the Freedesktop.org base directory specification'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-BaseDir-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::Which)
BuildRequires : perl(IPC::System::Simple)

%description
File-BaseDir
============
This module can be used to find directories and files as specified
by the Freedekstop.org Base Directory Specification.

%package dev
Summary: dev components for the perl-File-BaseDir package.
Group: Development
Provides: perl-File-BaseDir-devel = %{version}-%{release}

%description dev
dev components for the perl-File-BaseDir package.


%package license
Summary: license components for the perl-File-BaseDir package.
Group: Default

%description license
license components for the perl-File-BaseDir package.


%prep
%setup -q -n File-BaseDir-0.08
cd ..
%setup -q -T -D -n File-BaseDir-0.08 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-BaseDir-0.08/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-BaseDir
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-File-BaseDir/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/File/BaseDir.pm
/usr/lib/perl5/vendor_perl/5.28.1/File/IconTheme.pm
/usr/lib/perl5/vendor_perl/5.28.1/File/UserDirs.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::BaseDir.3
/usr/share/man/man3/File::IconTheme.3
/usr/share/man/man3/File::UserDirs.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-BaseDir/deblicense_copyright
