# revision 15878
# category Package
# catalog-ctan /macros/plain/contrib/hyplain
# catalog-date 2007-03-07 20:05:57 +0100
# catalog-license pd
# catalog-version 1.0
Name:		texlive-hyplain
Version:	1.0
Release:	1
Summary:	Basic support for multiple languages in Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/hyplain
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyplain.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyplain.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package offers a means to set up hyphenation suitable for
several languages and/or dialects, and to select them or switch
between them while typesetting.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
