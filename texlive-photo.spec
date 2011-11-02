Name:		texlive-photo
Version:	20061202
Release:	1
Summary:	A float environment for photographs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/photo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/photo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/photo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/photo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package introduces a new float type called photo which
works similar to the float types table and figure. Various
options exist for placing photos, captions, and a
"photographer" line. In twocolumn documents, a possibility
exists to generate double-column floats automatically if the
photo does not fit into one column. Photos do not have to be
placed as floats, they can also be placed as boxes, with
captions and photographer line still being available.

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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
