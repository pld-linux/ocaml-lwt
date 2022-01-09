#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Promises and event-driven I/O for OCaml
Summary(pl.UTF-8):	Obietnice i we/wy sterowane zdarzeniami dla OCamla
Name:		ocaml-lwt
Version:	5.4.2
Release:	3
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/ocsigen/lwt/releases
Source0:	https://github.com/ocsigen/lwt/archive/%{version}/lwt-%{version}.tar.gz
# Source0-md5:	ba3659a8918d8e7cb0f4ef9a83945f90
URL:		https://github.com/ocsigen/lwt
BuildRequires:	cppo >= 1.1.0
BuildRequires:	ocaml >= 1:4.08
BuildRequires:	ocaml-dune-devel >= 1.8.0
BuildRequires:	ocaml-findlib >= 1.7.3
BuildRequires:	ocaml-luv-devel
BuildRequires:	ocaml-mmap-devel >= 1.1.0
BuildRequires:	ocaml-ocplib-endian-devel
BuildRequires:	ocaml-ppxlib-devel >= 0.16.0
BuildRequires:	ocaml-react-devel >= 1.0.0
BuildRequires:	ocaml-result-devel
BuildRequires:	ocaml-seq-devel
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{without ocaml_opt}
%define		no_install_post_strip	1
# no opt means no native binary, stripping bytecode breaks such programs
%define		_enable_debug_packages	0
%endif

%description
A promise is a value that may become determined in the future.

Lwt provides typed, composable promises. Promises that are resolved by
I/O are resolved by Lwt in parallel.

Meanwhile, OCaml code, including code creating and waiting on
promises, runs in a single thread by default. This reduces the need
for locks or other synchronization primitives. Code can be run in
parallel on an opt-in basis.

%description -l pl.UTF-8
Obietnica (promise) to wartość, która może zostać określona w
przyszłości.

Lwt udostępnia typowane, składalne obietnice. Obietnice rozwiązywane
poprzez we/wy są rozwiązywane przez Lwt równolegle.

W międzyczasie kod w OCamlu, w tym kod tworzący i oczekujący na
obietnice, działa domyślnie w jednym wątku. Ogranicza to potrzebę
blokad lub innych mechanizmów synchronizacji. Kod może opcjonalnie
działać równolegle.

%package devel
Summary:	Promises and event-driven I/O for OCaml - development part
Summary(pl.UTF-8):	Obietnice i we/wy sterowane zdarzeniami dla OCamla - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
Lwt library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki Lwt.

%package luv
Summary:	Libuv engine for Lwt OCaml library
Summary(pl.UTF-8):	Silnik libuv dla biblioteki OCamla Lwt
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ocaml-luv
Requires:	ocaml-result

%description luv
Libuv engine for Lwt OCaml library.

%description luv -l pl.UTF-8
Silnik libuv dla biblioteki OCamla Lwt.

%package luv-devel
Summary:	Libuv engine for Lwt OCaml library - development part
Summary(pl.UTF-8):	Silnik libuv dla biblioteki OCamla Lwt - część programistyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-luv = %{version}-%{release}
Requires:	ocaml-luv-devel
Requires:	ocaml-result-devel

%description luv-devel
This package contains files needed to develop OCaml programs using
Lwt-luv library.

%description luv-devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki Lwt-luv.

%package ppx
Summary:	PPX syntax for OCaml Lwt library
Summary(pl.UTF-8):	Składnia PPX dla biblioteki OCamla Lwt
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ocaml-ppxlib >= 0.16.0

%description ppx
PPX syntax for Lwt, providing something similar to async/await from
JavaScript.

%description ppx -l pl.UTF-8
Składnia PPX dla Lwt, udostępniająca coś w stylu async/await z
JavaScriptu.

%package ppx-devel
Summary:	PPX syntax for OCaml Lwt library - development part
Summary(pl.UTF-8):	Składnia PPX dla biblioteki OCamla Lwt - część programistyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-ppx = %{version}-%{release}
Requires:	ocaml-ppxlib-devel >= 0.16.0

%description ppx-devel
This package contains files needed to develop OCaml programs using
Lwt-ppx library.

%description ppx-devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki Lwt-ppx.

%package react
Summary:	Helpers for using OCaml React library with Lwt
Summary(pl.UTF-8):	Funkcje pomocnicze do używania biblioteki OCamla React z Lwt
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ocaml-react >= 1.0.0

%description react
Helpers for using OCaml React library with Lwt.

%description react -l pl.UTF-8
Funkcje pomocnicze do używania biblioteki OCamla React z Lwt.

%package react-devel
Summary:	Helpers for using OCaml React library with Lwt - development part
Summary(pl.UTF-8):	Funkcje pomocnicze do używania biblioteki OCamla React z Lwt - część programistyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-react = %{version}-%{release}
Requires:	ocaml-react-devel >= 1.0.0

%description react-devel
This package contains files needed to develop OCaml programs using
Lwt-react library.

%description react-devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki Lwt-react.

%prep
%setup -q -n lwt-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/lwt/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/lwt/unix/*.{h,ml}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/lwt_{luv,ppx,react}/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/{lwt,lwt_luv,lwt_ppx,lwt_react}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE.md README.md
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllwt_unix_stubs.so
%dir %{_libdir}/ocaml/lwt
%{_libdir}/ocaml/lwt/META
%{_libdir}/ocaml/lwt/*.cma
%dir %{_libdir}/ocaml/lwt/unix
%{_libdir}/ocaml/lwt/unix/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lwt/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/lwt/unix/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lwt/*.cmi
%{_libdir}/ocaml/lwt/*.cmt
%{_libdir}/ocaml/lwt/*.cmti
%{_libdir}/ocaml/lwt/*.mli
%{_libdir}/ocaml/lwt/unix/*.cmi
%{_libdir}/ocaml/lwt/unix/*.cmt
%{_libdir}/ocaml/lwt/unix/*.cmti
%{_libdir}/ocaml/lwt/unix/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/lwt/*.a
%{_libdir}/ocaml/lwt/*.cmx
%{_libdir}/ocaml/lwt/*.cmxa
%{_libdir}/ocaml/lwt/unix/*.a
%{_libdir}/ocaml/lwt/unix/*.cmx
%{_libdir}/ocaml/lwt/unix/*.cmxa
%endif
%{_libdir}/ocaml/lwt/dune-package
%{_libdir}/ocaml/lwt/opam

%files luv
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/lwt_luv
%{_libdir}/ocaml/lwt_luv/META
%{_libdir}/ocaml/lwt_luv/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lwt_luv/*.cmxs
%endif

%files luv-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lwt_luv/*.cmi
%{_libdir}/ocaml/lwt_luv/*.cmt
%{_libdir}/ocaml/lwt_luv/*.cmti
%{_libdir}/ocaml/lwt_luv/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/lwt_luv/*.a
%{_libdir}/ocaml/lwt_luv/*.cmx
%{_libdir}/ocaml/lwt_luv/*.cmxa
%endif
%{_libdir}/ocaml/lwt_luv/dune-package
%{_libdir}/ocaml/lwt_luv/opam

%files ppx
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/lwt_ppx
%{_libdir}/ocaml/lwt_ppx/META
%{_libdir}/ocaml/lwt_ppx/*.cma
%attr(755,root,root) %{_libdir}/ocaml/lwt_ppx/ppx.exe
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lwt_ppx/*.cmxs
%endif

%files ppx-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lwt_ppx/*.cmi
%{_libdir}/ocaml/lwt_ppx/*.cmt
%{_libdir}/ocaml/lwt_ppx/*.cmti
%{_libdir}/ocaml/lwt_ppx/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/lwt_ppx/*.a
%{_libdir}/ocaml/lwt_ppx/*.cmx
%{_libdir}/ocaml/lwt_ppx/*.cmxa
%endif
%{_libdir}/ocaml/lwt_ppx/dune-package
%{_libdir}/ocaml/lwt_ppx/opam

%files react
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/lwt_react
%{_libdir}/ocaml/lwt_react/META
%{_libdir}/ocaml/lwt_react/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lwt_react/*.cmxs
%endif

%files react-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lwt_react/*.cmi
%{_libdir}/ocaml/lwt_react/*.cmt
%{_libdir}/ocaml/lwt_react/*.cmti
%{_libdir}/ocaml/lwt_react/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/lwt_react/*.a
%{_libdir}/ocaml/lwt_react/*.cmx
%{_libdir}/ocaml/lwt_react/*.cmxa
%endif
%{_libdir}/ocaml/lwt_react/dune-package
%{_libdir}/ocaml/lwt_react/opam
