def header2Dic(str):
    result = ['\'']
    for c in str:
        if c == ':':
            result.append('\'')
            result.append(c)
            result.append('\'')
        elif c == '\n':
            result.append('\'')
            result.append(',')
            result.append(c)
            result.append('\'')
        elif c == '\r' or c == ' ':
            continue
        else:
            result.append(c)
    return ''.join(result)

def cookies2Dic(str):
    result = ['\'']
    for c in str:
        if c == '	':
            result.append('\'')
            result.append(':')
            result.append('\'')
            continue
        elif c == '\n':
            result.append('\'')
            result.append(',')
            result.append('\n')
            result.append('\'')
        else:
            result.append(c)
    return ''.join(result)


str = """
overseaPurchaseCookies	
vendorRemarks	[{"venderId":"62710","remark":""}]
submitOrderParam.sopNotPutInvoice	true
submitOrderParam.trackID	TestTrackId
submitOrderParam.ignorePriceChange	0
submitOrderParam.btSupport	0
submitOrderParam.eid	2NHYCD75HVHYYFLNK2VL3SZHGCJG4A2RORK6MF2UZCMT3G2LZSESKSZHYSK6ZYMGQ6JL7P3WUTO3ZVNYXTBG25MSDU
submitOrderParam.fp	c2a009aec6339079c3a0c78eafe08816
riskControl	D0E404CB705B9732FD97C4DFCA0B7A95B67DC1EAD150767F35CF7976744D2B1AB4DDE2EB88B501AC
submitOrderParam.jxj	1
submitOrderParam.trackId	8517a2ea6c588e2d7a3540034e7bfe37
"""
print(cookies2Dic(str))
