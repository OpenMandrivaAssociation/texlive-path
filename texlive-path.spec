# revision 22045
# category Package
# catalog-ctan /macros/generic/path
# catalog-date 2011-04-07 22:08:26 +0200
# catalog-license other-free
# catalog-version 3.05
Name:		texlive-path
Version:	3.05
Release:	1
Summary:	Typeset paths, making them breakable
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/path
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/path.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/path.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Defines a macro \path|...|, similar to the LaTeX \verb|...|,
that sets the text in typewriter font and allows hyphen-less
breaks at punctuation characters. The set of characters to be
regarded as punctuation may be changed from the package's
default.

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
%{_texmfdistdir}/tex/generic/path/path.sty
%doc %{_texmfdistdir}/doc/generic/path/path-doc.pdf
%doc %{_texmfdistdir}/doc/generic/path/path-doc.tex
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
