%define packagename tclaugeas

Name:           tcl-augeas
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  tcl-devel
BuildRequires:  augeas-devel >= 0.10
Version:        0.4.0
Release:        0
Summary:        Tcl bindings for Augeas
License:        MIT
Group:          Development/Languages/Tcl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
URL:            https://github.com/dbohdan/tcl-augeas
Source0:        %name-%version.tar.gz

%description
This C extension for the Tcl interpreter provides bindings for Augeas,
a configuration editing tool.
    
%prep
%setup -q -n %{name}-%{version}

%build
%configure \
	--with-tcl=%_libdir \
	--enable-threads
make

%install
make install DESTDIR=%buildroot pkglibdir=%tcl_archdir/%{packagename}%{version}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%tcl_archdir
%doc AUTHORS LICENSE README.md

%changelog
