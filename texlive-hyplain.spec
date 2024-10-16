Name:		texlive-hyplain
Version:	15878
Release:	2
Summary:	Basic support for multiple languages in Plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/hyplain
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyplain.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyplain.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers a means to set up hyphenation suitable for
several languages and/or dialects, and to select them or switch
between them while typesetting.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/hyplain/hylang.tex
%{_texmfdistdir}/tex/plain/hyplain/hypdfplain.ini
%{_texmfdistdir}/tex/plain/hyplain/hyplain.tex
%{_texmfdistdir}/tex/plain/hyplain/hyrules.tex
%doc %{_texmfdistdir}/doc/plain/hyplain/README
%doc %{_texmfdistdir}/doc/plain/hyplain/hydoc.pdf
%doc %{_texmfdistdir}/doc/plain/hyplain/hydoc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
