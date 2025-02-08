import tkinter as tk
from tkinter import messagebox
import random

class MonsterGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Monster Evolution Game")
        
        # Monster initial stats
        self.level = 1
        self.xp = 0
        self.max_xp = 100
        self.energy = 100
        self.attack = 10
        self.defense = 5
        self.speed = 3
        self.evolution_stage = 0
        
        # GUI Setup
        self.create_widgets()
        self.update_display()
        
        # Menu Setup
        self.create_menu()

    def create_widgets(self):
        # Monster Display
        self.monster_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.monster_frame.pack(pady=10)
        
        self.monster_label = tk.Label(self.monster_frame, text="", font=('Courier', 20))
        self.monster_label.pack(padx=20, pady=10)
        
        # Stats Display
        self.stats_frame = tk.Frame(self.root)
        self.stats_frame.pack(pady=5)
        
        self.stats_labels = {
            'level': tk.Label(self.stats_frame, text="Level: 1"),
            'xp': tk.Label(self.stats_frame, text="XP: 0/100"),
            'energy': tk.Label(self.stats_frame, text="Energy: 100"),
            'attack': tk.Label(self.stats_frame, text="Attack: 10"),
            'defense': tk.Label(self.stats_frame, text="Defense: 5"),
            'speed': tk.Label(self.stats_frame, text="Speed: 3")
        }
        for label in self.stats_labels.values():
            label.pack(side=tk.LEFT, padx=10)
            
        # Actions Frame
        self.actions_frame = tk.Frame(self.root)
        self.actions_frame.pack(pady=10)
        
        self.btn_train = tk.Button(self.actions_frame, text="Train", command=self.train)
        self.btn_train.pack(side=tk.LEFT, padx=5)
        
        self.btn_rest = tk.Button(self.actions_frame, text="Rest", command=self.rest)
        self.btn_rest.pack(side=tk.LEFT, padx=5)
        
        self.btn_battle = tk.Button(self.actions_frame, text="Battle", command=self.battle)
        self.btn_battle.pack(side=tk.LEFT, padx=5)
        
        self.btn_stats = tk.Button(self.actions_frame, text="Full Stats", command=self.show_stats)
        self.btn_stats.pack(side=tk.LEFT, padx=5)

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def update_display(self):
        # Update monster appearance based on level
        monster_art = [
            "🟩",  # Level 1
            "🟥\n🟩",  # Level 2
            "🟥🟦\n🟩🟨",  # Level 3
            "🟥🟥🟥\n🟦🟦🟦\n🟩🟩🟩"  # Level 4
        ]
        self.monster_label.config(text=monster_art[min(self.level//5, 3)])
        
        # Update stats labels
        self.stats_labels['level'].config(text=f"Level: {self.level}")
        self.stats_labels['xp'].config(text=f"XP: {self.xp}/{self.max_xp}")
        self.stats_labels['energy'].config(text=f"Energy: {self.energy}")
        self.stats_labels['attack'].config(text=f"Attack: {self.attack}")
        self.stats_labels['defense'].config(text=f"Defense: {self.defense}")
        self.stats_labels['speed'].config(text=f"Speed: {self.speed}")

    def train(self):
        if self.energy >= 20:
            gained_xp = random.randint(15, 25)
            self.xp += gained_xp
            self.energy -= 20
            self.check_level_up()
            self.update_display()
            messagebox.showinfo("Training", f"You gained {gained_xp} XP!")
        else:
            messagebox.showwarning("Low Energy", "Not enough energy to train!")

    def rest(self):
        recovered = random.randint(20, 40)
        self.energy = min(100, self.energy + recovered)
        self.update_display()
        messagebox.showinfo("Resting", f"You recovered {recovered} energy!")

    def battle(self):
        if self.energy >= 30:
            outcome = random.choice(['win', 'lose'])
            if outcome == 'win':
                gained_xp = random.randint(30, 50)
                self.xp += gained_xp
                messagebox.showinfo("Battle", f"You won and gained {gained_xp} XP!")
            else:
                self.energy -= 15
                messagebox.showinfo("Battle", "You lost the battle!")
            self.energy -= 30
            self.check_level_up()
            self.update_display()
        else:
            messagebox.showwarning("Low Energy", "Not enough energy to battle!")

    def check_level_up(self):
        if self.xp >= self.max_xp:
            self.level += 1
            self.xp = 0
            self.max_xp = int(self.max_xp * 1.5)
            
            # Stat increases
            self.attack += random.randint(2, 5)
            self.defense += random.randint(1, 4)
            self.speed += random.randint(1, 3)
            
            messagebox.showinfo("Level Up!", f"Congratulations! You reached level {self.level}!")
            self.update_display()

    def show_stats(self):
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Detailed Stats")
        
        stats_text = f"""
        -- Monster Stats --
        Level: {self.level}
        XP: {self.xp}/{self.max_xp}
        Energy: {self.energy}
        
        Attack: {self.attack}
        Defense: {self.defense}
        Speed: {self.speed}
        
        Evolution Stage: {min(self.level//5, 3)}
        """
        tk.Label(stats_window, text=stats_text).pack(padx=20, pady=10)

    def show_about(self):
        messagebox.showinfo("About", "Monster Evolution Game\nCreated with Python Tkinter")

if __name__ == "__main__":
    root = tk.Tk()
    game = MonsterGame(root)
    root.mainloop()
