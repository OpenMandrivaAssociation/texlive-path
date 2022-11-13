Name:		texlive-path
Version:	22045
Release:	1
Summary:	Typeset paths, making them breakable
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/path
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/path.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/path.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines a macro \path|...|, similar to the LaTeX \verb|...|,
that sets the text in typewriter font and allows hyphen-less
breaks at punctuation characters. The set of characters to be
regarded as punctuation may be changed from the package's
default.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/path/path.sty
%doc %{_texmfdistdir}/doc/generic/path/path-doc.pdf
%doc %{_texmfdistdir}/doc/generic/path/path-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
