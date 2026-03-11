using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Greetings.Models;

namespace Greetings.Data
{
    public class AppDbContext : DbContext
    {
        public DbSet<Family> Families { get; set; }
        public DbSet<Person> People { get; set; }
        public DbSet<Car> Cars { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder options)
        {
            options.UseSqlite("Data Source=GreetingsDB.sqlite");
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            // Define One-to-Many relationships explicitly
            modelBuilder.Entity<Family>()
                .HasMany(f => f.Members)
                .WithOne(p => p.Family)
                .HasForeignKey(p => p.FamilyId);

            modelBuilder.Entity<Family>()
                .HasMany(f => f.Vehicles)
                .WithOne(c => c.Family)
                .HasForeignKey(c => c.FamilyId);
        }
    }
}
