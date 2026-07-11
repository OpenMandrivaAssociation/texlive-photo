%global tl_name photo
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A float environment for photographs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/photo
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/photo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/photo.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/photo.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package introduces a new float type called photo which works
similar to the float types table and figure. Various options exist for
placing photos, captions, and a "photographer" line. In twocolumn
documents, a possibility exists to generate double-column floats
automatically if the photo does not fit into one column. Photos do not
have to be placed as floats, they can also be placed as boxes, with
captions and photographer line still being available.

