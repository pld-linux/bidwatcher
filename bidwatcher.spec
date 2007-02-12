Summary:	Track and snipe eBay auctions
Summary(pl.UTF-8):   Śledzenie i licytowanie aukcji eBay
Name:		bidwatcher
Version:	1.3.17
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/bidwatcher/%{name}-%{version}.tar.gz
# Source0-md5:	ea576cb86dcf36abe18436e0eba15a30
URL:		http://bidwatcher.sourceforge.net/
BuildRequires:	gtk+-devel >= 1.2.10
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bidwatcher is a tool for eBay users. It is a stand alone application
that can track auctions and perform automated bids called 'snipes'.

%description -l pl.UTF-8
Bidwatcher to narzędzie przeznaczone dla użytkowników serwisu
aukcyjnego eBay. Jest to samodzielna aplikacja pozwalająca śledzić
aukcje, automatyzować licytacje.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README quick_start.html
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}*
