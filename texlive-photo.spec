Name:		texlive-photo
Version:	18739
Release:	1
Summary:	A float environment for photographs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/photo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/photo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/photo.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/photo.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package introduces a new float type called photo which
works similar to the float types table and figure. Various
options exist for placing photos, captions, and a
"photographer" line. In twocolumn documents, a possibility
exists to generate double-column floats automatically if the
photo does not fit into one column. Photos do not have to be
placed as floats, they can also be placed as boxes, with
captions and photographer line still being available.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/photo/photo.sty
%doc %{_texmfdistdir}/doc/latex/photo/Makefile
%doc %{_texmfdistdir}/doc/latex/photo/photo.pdf
%doc %{_texmfdistdir}/doc/latex/photo/photo_test.tex
#- source
%doc %{_texmfdistdir}/source/latex/photo/photo.drv
%doc %{_texmfdistdir}/source/latex/photo/photo.dtx
%doc %{_texmfdistdir}/source/latex/photo/photo.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
