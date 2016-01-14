%global pkg_name jboss-servlet-3.0-api
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.0.1
Release:          9.9%{?dist}
Summary:          Java Servlet 3.0 API
License:          CDDL
Url:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-servlet-api_spec.git
# cd jboss-servlet-api_spec/ && git archive --format=tar --prefix=jboss-servlet-3.0-api/ jboss-servlet-api_3.0_spec-1.0.1.Final | xz > jboss-servlet-3.0-api-1.0.1.Final.tar.xz
Source0:          jboss-servlet-3.0-api-%{namedversion}.tar.xz

BuildRequires:    %{?scl_prefix}jboss-specs-parent
BuildRequires:    %{?scl_prefix_java_common}javapackages-tools
BuildRequires:    %{?scl_prefix_java_common}maven-local
BuildRequires:    %{?scl_prefix}maven-compiler-plugin
BuildRequires:    %{?scl_prefix}maven-install-plugin
BuildRequires:    %{?scl_prefix}maven-jar-plugin
BuildRequires:    %{?scl_prefix}maven-javadoc-plugin
BuildRequires:    %{?scl_prefix}maven-enforcer-plugin
BuildRequires:    %{?scl_prefix}maven-dependency-plugin

BuildArch:        noarch

%description
The Java Servlet 3.0 API classes.

%package javadoc
Summary:          Javadocs for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n jboss-servlet-3.0-api
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.0.1-9.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.0.1-9.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-9.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-9.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-9.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-9.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-9.3
- SCL-ize build-requires
- Migrate from mvn-rpmbuild to %%mvn_build

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-9.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-9.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.1-9
- Mass rebuild 2013-12-27

* Fri Dec 13 2013 Ade Lee <alee@redhat.com> 1.0.1-8
- Fix spec file dist tag for rpmlint

* Wed Nov 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-7
- Remove unneeded BR: maven-plugin-cobertura

* Thu May 9 2013 Ade Lee <alee@redhat.com> 1.0.1-6
- Resolves #961462 - Remove unneeded maven-checkstyle-plugin and 
  maven-eclipse-plugin BR

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> - 1.0.1-3
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Upstream release 1.0.1.Final
- Added mapping to javax.servlet:servlet-api

* Thu Aug 11 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-0.1.20120312gitd4b6f2
- Packaging after license cleanup
- Spec cleanup

* Thu Aug 11 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging
