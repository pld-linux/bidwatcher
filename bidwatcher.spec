Summary:	Track and snipe eBay auctions
Summary(pl):	¦ledzenie i licytowanie aukcji eBay
Name:		bidwatcher
Version:	1.3.11
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	6917d747d8e1ca6e8ec44d78d1720c3f
BuildRequires:	gtk+-devel >= 1.2.10
BuildRequires:	libstdc++-devel
URL:		http://bidwatcher.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bidwatcher is a tool for eBay users. It is a stand alone application
that can track auctions and perform automated bids called 'snipes'.

%description -l pl
Bidwatcher to narzêdzie przeznaczone dla u¿ytkowników serwisu
aukcyjnego eBay. Jest to samodzielna aplikacja pozwalaj±ca ¶ledziæ
auktcje, automatyzowaæ licytacje.

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
