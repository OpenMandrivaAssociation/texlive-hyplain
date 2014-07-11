# revision 15878
# category Package
# catalog-ctan /macros/plain/contrib/hyplain
# catalog-date 2007-03-07 20:05:57 +0100
# catalog-license pd
# catalog-version 1.0
Name:		texlive-hyplain
Version:	1.0
Release:	8
Summary:	Basic support for multiple languages in Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/hyplain
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyplain.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyplain.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752681
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718689
- texlive-hyplain
- texlive-hyplain
- texlive-hyplain
- texlive-hyplain

