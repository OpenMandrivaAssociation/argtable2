%define major 0
%define libname %mklibname argtable2 %{major}
%define devname %mklibname argtable2 -d

Name: argtable2
Version: 2.13
Release: 2
Source0: http://prdownloads.sf.net/argtable/argtable%(echo %{version} |cut -d. -f1)-%(echo %{version} |cut -d. -f2-).tar.gz
Summary: An ANSI C command line parser
URL: http://argtable.sf.net/
License: GPL
Group: System/Libraries

%description
Argtable is an ANSI C library for parsing GNU style command line options with
a minimum of fuss.

It enables a program's command line syntax to be defined in the source code
as an array of argtable structs. The command line is then parsed according to
that specification and the resulting values are returned in those same structs
where they are accessible to the main program.

Both tagged (-v, --verbose, --foo=bar) and untagged arguments are supported,
as are multiple instances of each argument. Syntax error handling is
automatic and the library also provides the means for generating a textual
description of the command line syntax.

%package -n %{libname}
Summary: An ANSI C command line parser
Group: System/Libraries

%description -n %{libname}
Argtable is an ANSI C library for parsing GNU style command line options with
a minimum of fuss.

It enables a program's command line syntax to be defined in the source code
as an array of argtable structs. The command line is then parsed according to
that specification and the resulting values are returned in those same structs
where they are accessible to the main program.

Both tagged (-v, --verbose, --foo=bar) and untagged arguments are supported,
as are multiple instances of each argument. Syntax error handling is
automatic and the library also provides the means for generating a textual
description of the command line syntax.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Argtable is an ANSI C library for parsing GNU style command line options with
a minimum of fuss.

It enables a program's command line syntax to be defined in the source code
as an array of argtable structs. The command line is then parsed according to
that specification and the resulting values are returned in those same structs
where they are accessible to the main program.

Both tagged (-v, --verbose, --foo=bar) and untagged arguments are supported,
as are multiple instances of each argument. Syntax error handling is
automatic and the library also provides the means for generating a textual
description of the command line syntax.

%prep
%setup -qn argtable%(echo %{version} |cut -d. -f1)-%(echo %{version} |cut -d. -f2-)
%configure

%build
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%doc %{_docdir}/%{name}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*
