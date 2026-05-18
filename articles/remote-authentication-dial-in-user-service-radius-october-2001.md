---
title: "Remote Authentication Dial-in User Service (RADIUS)"
publication: "Informatics"
issue_date: "October 2001"
pages: [21, 22]
author: null
section: "Technology & Services"
---

## Remote Authentication Dial-in User Service (RADIUS)

NIC is providing dialup Internet facility to users from more than 20 locations. Till now, different locations were using different means for authentication like tacacs, local, tacacs+ , third party software etc. There was no AAA (Authentication, Authorisation and Accounting) standard being followed from the various offices. The Internet Services Group of NIC has taken the task of implementing the AAA standard in all offices of NIC. Radius (Remote Authentication Dial In User Service) is the protocol used for implementing the AAA solution. The code runs on Solaris/ Linux. Radius Technology has been selected for the purpose as it is now the industry standard. It uses UDP and can assign various restrictions and privileges to users dynamically. Radius supports Roaming facility and users can be restricted on group, login basis etc. Radius support is available on almost all NAS devices. In the first phase of the Project, the radius software was installed and configured with the local NAS. While installing, five standard groups were also made in the system namely: free, paid, staff, popfree and poppaid. Basically FREE and PAID groups are for internet users and POPFREE and POPPAID group are for ‘email-only’ users. The Staff group is for NIC staff. While creating the users it was requested that a dialup user should be one of these five groups for dialup access. Thus this enables a uniform grouping policy for dialup. Each group has its own authorization features for e.g the users in the Free and Paid group can access all internet services while the users in the POPFREE and POPPAID groups, can access inside the NIC. Accounting scripts were also installed during this phase and a half day training was organised. A web based password change facility was also implemented for the users of these locations. Now users can change their password through the web URL www.ren.nic.in In the second phase roaming facility was implemented. Now the dialup users of 20 cities listed in the table can be authenticated from all the listed places for accesing the network. Hence there is no need for creating the multiple user-ids at different locations for the same user and the users can roam among these 20 locations. Example: Suppose “xyz” is the username created at Delhi and the user wants to use the dialup from Mumbai. The user has to dial the local number of Mumbai NIC office as listed in the table given below and give the username as xyz@pppdel Rest of the procedure remains the same. The RADIUS will authenticate the user from Delhi. In the next phase technologies such as ISDN line authentication, use of calling telephone number with username and password to provide further credibility to authentication mechanism, web based radwho, usage display from same web location etc may be also be implemented.

Roaming Table

ROAMING
S.No LOCATION DIAL UP Nos Support (Email & Voice)
SUFFIX

1 Delhi pppdel 4882222, 4366878, 6795, 5518, 5589, 6887, 6315, 3360, 3431,4360084, 4360088 support@nic.in Voice: (011)

2 Panipat pppnp 653422, 653464, 659476 support@pnp.nic.in Voice :01742-653468, 951742-653468 (from Delhi)

3 Goa pppgoa 424557, support@goa.nic.in Voice : (0832)225702

4 Pondichery pppondy 342013, support@pondy.pon.nic.in Voice : 336675

5 Bhopal pppbhopal 558256, 760853 support@mp.nic.in Voice : (0755)558299

6 Tripura* ppptrp 322947, support@trp.nic.in Voice : (0381) 327373

7 Pune ppppune 5537737, 736, 5538116, 115,117, 125, 126, 127,128 support@mah.nic.in Voice: (020) 5534832/ 5534732 Extn 4110/ 4111

8 Bangalore pppkar 5537125, 5537130, 5522925, 5522865 support@kar.nic.in Voice : (080) 5537123, 5522432

9 Chennai ppptn 4461160, 4900028 support@tn.nic.in Voice No (044) 4917850, 4902580, 4466495

10 Gujarat pppguj 3228860, 3228871 support@guj.nic.in Voice :(079) 3252946,3252408

11 Kolkata pppkol 2808690, 2810130 support@wb.nic.in Voice : (033) 2407320

12 Jaipur pppraj 364183, support@raj.nic.in Voice : (0141)373561

13 Cochin pppcochin 423013, 014, 015, 422892, 422901, 422910 support@ker.nic.in, Voice : (0484) 423769

14 Bhuwaneshwar pppbhuv 402321, 2328, 2329, 2342, 2346, 2358, 2362, 7409, 411217, 7970, 7971, 7972, 7973, 7974, 7975 support@ori.nic.in Voice : (0674) 411592

15 Hyderabad pphyd 3220148, 3222148, 3228123, 3223169, 3221440, 3221940, 3223943, 3228442, 3222137, 3222124, 3222125, 3222116, 3222145 support@ap.nic.in Voice : (040) 3224573

16 Chandigarh pppchd 544119, 544350 (email) support@chd.nic.in, Voice : (0172) 544349, 778343

17 Bihar pppbihar 212517, 239471 support@bih.nic.in Voice: (0612) 239474

18 Lucknow pppluck 28-0193, 0994, 1210, 1250, 1335, 1529, 1535, 1550, 0544, 0546, 0548,0550 support@up.nic.in Voice: (0522) 280511, 280424

19 Andman pppand 33486, 32277, 45798 support@and.nic.in, sio@and.nic.in Voice (03192) 32733

20 Haryana ppphry 74-3841,2986, 1689 support@hry.nic.in Voice: (0172) 741950

21 Mumbai pppmbai 7561222, 7561253 support@bom.nic.in Voice : (022) 7576824, 7575783, Fax : 2853562

22 Vizag pppvizag 505922, 505927 support@itpvis.ap.nic.in Voice : (0891) 505928
