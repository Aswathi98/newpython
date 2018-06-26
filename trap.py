from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    sendNotification(
        SnmpEngine(OctetString(hexValue='8000000001020304')),
        UsmUserData('usr-sha-aes128', 'authkey1', 'privkey1',
                    authProtocol=usmHMACSHAAuthProtocol,
                    privProtocol=usmAesCfb128Protocol),
        UdpTransportTarget(('demo.snmplabs.com', 162)),
        ContextData(),
        'trap',
        NotificationType(ObjectIdentity('SNMPv2-MIB', 'authenticationFailure'))
    )
)

if errorIndication:
    print(errorIndication)
