Name:		texlive-semantic-markup
Version:	53607
Release:	2
Summary:	Meaningful semantic markup in the spirit of the Text Encoding Initiative
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/semantic-markup
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semantic-markup.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semantic-markup.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides simple commands to allow authors
(especially scholars in the humanities) to write with a focus
on content rather than presentation. The commands are inspired
by the XML elements of the Text Encoding Initiative. Commands
like \term and \foreign are aliases for \emph. \quoted and
\soCalled are aliases for quoting commands. These commands
could be easily redefined for different formats. The package
also provides a footnote environment so that long footnotes can
be more cleanly separated from the main text. Because the
author is a music scholar, the package also includes some
macros for musical symbols and other basic notations for
musical analysis.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/semantic-markup
%doc %{_texmfdistdir}/doc/latex/semantic-markup

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
