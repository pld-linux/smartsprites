# TODO
# - full system jars
%include	/usr/lib/rpm/macros.java
Summary:	Smart Sprites - CSS Sprite Generator Done Right
Name:		smartsprites
Version:	0.2.8
Release:	0.1
License:	BSD
Group:		Development/Languages/Java
Source0:	http://csssprites.org/download/%{name}-%{version}.zip
# Source0-md5:	35fe7d57b84614f9343fba7cfd13d3ab
Source1:	%{name}.sh
URL:		http://csssprites.org/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	java-commons-io >= 1.4
Requires:	java-commons-lang >= 2.3
#Requires:	java-commons-math >= 1.1
#Requires:	java-google-collections >= 1.0
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SmartSprites will let you easily introduce and maintain CSS sprites in
your designs. SmartSprites parses special directives you can insert
into your original CSS to mark individual images to be turned into
sprites. It then builds sprite images from the collected images and
automatically inserts the required CSS properties into your style
sheet, so that the sprites are used instead of the individual images.

%prep
%setup -q
%undos readme.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

cp -p lib/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# TODO
cp -p lib/commons-math-*.jar $RPM_BUILD_ROOT%{_javadir}
cp -p lib/google-collections-*.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt smartsprites.LICENSE
%attr(755,root,root) %{_bindir}/%{name}
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%{_javadir}/commons-math-*.jar
%{_javadir}/google-collections-*.jar
