# revision 18739
# category Package
# catalog-ctan /macros/latex/contrib/photo
# catalog-date 2006-12-02 15:26:11 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-photo
Version:	20061202
Release:	7
Summary:	A float environment for photographs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/photo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/photo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/photo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/photo.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061202-2
+ Revision: 754896
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061202-1
+ Revision: 719252
- texlive-photo
- texlive-photo
- texlive-photo
- texlive-photo

