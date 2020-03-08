// testsjj.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include "pch.h"
#include <stdio.h>
#include <stdlib.h>

inline void Sdk_Int2Char(int p_nNum, unsigned char *p_Ch)
{
	*p_Ch = (p_nNum <= 9) ? (p_nNum + '0') : ((p_nNum - 10) + 'A');
}

void Sdk_Str2BcdStr(unsigned char *p_Str, int p_nLen, unsigned char *p_StrBcd)
{
	int i = 0, j = 0;
	p_StrBcd[j++] = '0';
	p_StrBcd[j++] = 'x';
	for (i = 0; i < p_nLen; ++i)
	{
		Sdk_Int2Char((p_Str[i] >> 4) & 0x0F, &p_StrBcd[j++]);
		Sdk_Int2Char(p_Str[i] & 0x0F, &p_StrBcd[j++]);
	}
	p_StrBcd[j++] = '\0';
	return;
}

int main()
{
	unsigned char c_utc_time[6] = { 0x01, 0x70, 0xB3, 0xA3, 0x52, 0x30 };
	unsigned char result[50];
	Sdk_Str2BcdStr(c_utc_time, 6, result);
	printf("%s\n", result);
	char *str;
	long long i = strtoll((const char *)result, &str, 16);
	printf("%lld", i);
	getchar();
	return 0;
}
