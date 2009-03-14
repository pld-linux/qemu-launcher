%include	/usr/lib/rpm/macros.perl
Summary:	A GTK+ front-end for the Qemu x86 PC emulator
Summary(pl.UTF-8):	Interfejs GTK+ dla emulatora PC x86 Qemu
Name:		qemu-launcher
Version:	1.7.4
Release:	1
License:	GPL v2
Group:		Applications/Emulators
Source0:	http://download.gna.org/qemulaunch/1.7.x/%{name}_%{version}.tar.gz
# Source0-md5:	bd71fd543bd2723c7ea54de81f7ccabf
URL:		http://emeitner.f2o.org/qemu_launcher/
BuildRequires:	libxml2-progs
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qemu Launcher provides a graphical front-end to all basic, and many
advanced QEMU computer emulator options. It allows you to create,
save, and run multiple virtual machine configurations, create and
convert disk images.

Qemu Launcher utilizes the full system emulation mode of QEMU that
allows you to run unmodified operating system on virtual hardware.

Qemu Launcher also supports launching virtual machines from the
command line, by specifying the configuration name:

qemu-launcher 'Configuration name'

Note that you still need a graphical environment to do this, unless
the virtual machine is set to start in non-graphics mode.

%description -l pl.UTF-8
Qemu Launcher udostępnia graficzny interfejs do wszystkich
podstawowych i wielu zaawansowanych opcji emulatora komputera QEMU.
Pozwala na tworzenie, zapisywanie i uruchamianie wielu konfiguracji
maszyny wirtualnej oraz tworzenie i konwersję obrazów dysków.

Qemu Launcher wykorzystuje tryb pełnej emulacji systemu QEMU, co
pozwala na uruchamianie niemodyfikowanego systemu operacyjnego na
wirtualnym sprzęcie.

Qemu Launcher obsługuje także uruchamianie maszyn wirtualnych z linii
poleceń poprzez podanie nazwy konfiguracji:

qemu-launcher 'Nazwa konfiguracji'

Należy zauważyć, że do tego nadal potrzebne jest graficzne środowisko,
chyba że maszyna wirtualna została skonfigurowana do uruchamiania bez
trybu graficznego.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX="%{_prefix}" \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}
rm -fr $RPM_BUILD_ROOT%{_docdir}/qemu-launcher

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Changelog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/*/*
%{_pixmapsdir}/*.*
%{_mandir}/man1/*
