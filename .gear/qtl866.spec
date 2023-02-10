%define unpackaged_files_terminate_build 1

Name: qtl866-utils
Version: 1.0.0
Release: alt1

Summary: GUI driver for minipro EPROM/Device programmer software
License: %gpl3only

BuildRequires(pre): rpm-build-licenses
Group: Other
Url: https://github.com/wd5gnr/qtl866
Source0: %name-%version.tar

%description
GUI driver for minipro EPROM/Device programmer software

%prep
%setup -q

%build
%cmake
%install
%cmakeinstall_std
%files
%_bindir/qtl866
%_bindir/binhexedit
%_bindir/miniprohex

%changelog
* Tue Feb 10 2023 Aleksey Saprunov <sav@altlinux.org> 1.0.0-alt1
- Initial release

