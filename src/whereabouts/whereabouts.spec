%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}

Name: microshift
Version: %{version}
Release: %{release}%{dist}
Summary: Whereabouts CNI for MicroShift
License: ASL 2.0
URL: https://github.com/openshift/whereabouts-cni
Source0: https://github.com/openshift/microshift/archive/%{commit}/microshift-%{shortcommit}.tar.gz
ExclusiveArch: x86_64 aarch64

%description
The microshift package provides an OpenShift Kubernetes distribution optimized for small form factor and edge computing.

%prep
%setup -n microshift-%{commit}

%package whereabouts
Summary: Whereabouts CNI manifests for MicroShift
Requires: microshift = %{version}

%description whereabouts
The microshift-whereabouts package provides the label-gated Whereabouts CNI manifests.

%package whereabouts-release-info
Summary: Release information for Whereabouts CNI for MicroShift
BuildArch: noarch
Requires: microshift-release-info = %{version}

%description whereabouts-release-info
The microshift-whereabouts-release-info package provides Whereabouts image references for this release.

%install
install -d -m755 %{buildroot}/%{_prefix}/lib/microshift/manifests.d/002-microshift-whereabouts
install -p -m644 assets/optional/whereabouts/0* %{buildroot}/%{_prefix}/lib/microshift/manifests.d/002-microshift-whereabouts
install -p -m644 assets/optional/whereabouts/kustomization.yaml %{buildroot}/%{_prefix}/lib/microshift/manifests.d/002-microshift-whereabouts

%ifarch x86_64
cat assets/optional/whereabouts/kustomization.x86_64.yaml >> %{buildroot}/%{_prefix}/lib/microshift/manifests.d/002-microshift-whereabouts/kustomization.yaml
%endif
%ifarch %{arm} aarch64
cat assets/optional/whereabouts/kustomization.aarch64.yaml >> %{buildroot}/%{_prefix}/lib/microshift/manifests.d/002-microshift-whereabouts/kustomization.yaml
%endif

install -d -m755 %{buildroot}%{_datadir}/microshift/release
install -p -m644 assets/optional/whereabouts/release-whereabouts-{x86_64,aarch64}.json %{buildroot}%{_datadir}/microshift/release/

%files whereabouts
%dir %{_prefix}/lib/microshift/manifests.d/002-microshift-whereabouts
%{_prefix}/lib/microshift/manifests.d/002-microshift-whereabouts/*

%files whereabouts-release-info
%{_datadir}/microshift/release/release-whereabouts-{x86_64,aarch64}.json
