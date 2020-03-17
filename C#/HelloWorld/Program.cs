using System;
/*

Learn from docs.microsoft.com


 */
namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            string str_myFriend = "Tim";
            
            Console.WriteLine("Hello World!!!!");    
            //连接字符串和变量  +        
            Console.WriteLine("My friend is "+ str_myFriend);
            // 字符串内加入变量  $ {}
            Console.WriteLine($"My friend is {str_myFriend}  {str_myFriend}");// ___ print by $ and { }
            Console.WriteLine($"My friend is {str_myFriend} and his name has {str_myFriend.Length} letters");

            Console.WriteLine("\n----------------------------------------------\n");            
            //清除字符串前后的空格
            string str_greeting =  "        Hello World        ";
            Console.WriteLine($"[{str_greeting}]");//正常显示空格

            string str_trimmedGreeting = str_greeting.TrimStart();
            Console.WriteLine($"[{str_trimmedGreeting}]");// 清除字符串前的空格

            str_trimmedGreeting = str_greeting.TrimEnd();
            Console.WriteLine($"[{str_trimmedGreeting}]");// 清除字符串后的空格

            str_trimmedGreeting = str_greeting.Trim();
            Console.WriteLine($"[{str_trimmedGreeting}]");// 清除字符串内的前后空格


            Console.WriteLine("\n----------------------------------------------\n");
            //字符串替换
            string str_sayHello = "hello world";
            Console.WriteLine(str_sayHello);
            str_sayHello = str_sayHello.Replace("hello", "greeting");// 将 hello 替换为greeting
            Console.WriteLine(str_sayHello);
            //将字符串设为全部大写/小写
            Console.WriteLine(".ToUpper() :"+str_sayHello.ToUpper());
            Console.WriteLine(".ToLower() :"+str_sayHello.ToLower());


            Console.WriteLine("\n----------------------------------------------\n");
            //搜索字符串
            string str_songLyrics = "You say goodbye, and I say hello";
            Console.WriteLine(str_songLyrics.Contains("goodbye"));
            Console.WriteLine(str_songLyrics.Contains("gtrrtings"));

            // https://docs.microsoft.com/zh-cn/dotnet/csharp/tutorials/intro-to-csharp/hello-world?tutorial-step=5


        }
    }
}
