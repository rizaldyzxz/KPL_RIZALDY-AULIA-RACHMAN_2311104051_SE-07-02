using System;

class Program
{
    static void Main()
    {
        // Memanggil method SapaUser dari class HaloGeneric
        HaloGeneric halo = new HaloGeneric();
        halo.SapaUser("Rizaldy");

        // Menggunakan class DataGeneric untuk menyimpan dan mencetak data NIM
        DataGeneric<string> data = new DataGeneric<string>("2311104051");
        data.PrintData();
    }
}
