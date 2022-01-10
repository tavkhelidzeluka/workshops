# Python

<details>
    <summary>დავალებები</summary>

- [დავალება 1](https://forms.gle/GF8Z63eRmKc2QfUe8)

- [დავალება 2.1](https://forms.gle/CFSBXGK4DKFbPENj6)
- [დავალება 2.2](https://forms.gle/yyb9zzhBrZv2U3Mi9)

- [დავალება 3](https://forms.office.com/r/WYYLzU9sD2)

- [დავალება 4](https://forms.gle/KTE7a5H5Azk98F5p6)
- [დავალება 5.1](https://pastebin.com/F4qpp0eE)
- [დავალება 5.2](https://pastebin.com/v1AyEdc3)
    
 
</details>

<details>
    <summary>მასალები</summary>

- [Workshop 1](docs/WORKSHOP_1.md)
- [Workshop 2](docs/WORKSHOP_2.md)
- [Workshop 3](docs/WORKSHOP_3.md)

</details>

<details>
    <summary>რა უნდა ვიცოდეთ?</summary>

# MUST
1. MVT
2. GET/POST methods
2. MODELS (OTM (FK), MTM, Queryset API)
3. views (Function/Class) (CreateView, UpdateView, etc.)
4. templates
5. static files
6. media files
7. forms (ModelForm, Form)
8. admin (TabularInline, etc.)
9. auth


# Advanced topics
- prefetch_related, select_related (Advanced queryset API)
- DRF (django rest framework)
- hosting
- dns/domain
- nginx
- SSL

</details>



# Project requirements

Blog site

- მომხმარებელს უნდა შეეძლოს ავტორიზაცია (register/login)
- User: avatar, first_name, last_name, birth_date, username, email, password

- უნდა იყოს ბლოგისთვის საჭირო მოდელები: Post, Comment, Tag, Like
	- Post: user, title, background_image, body, create_date, edited_date, Tags (MTM)
	- Comment: user, text, Post (რომელ პოსტს ეკუთვნის)
	- Tag: title
	- Like: User, Post
- home page-ზე უნდა გამოჩნდეს 20-20 პოსტი (გამოიყენეთ pagination)
	- პოსტს უნდა უჩანდეს სათაური, ვინ შექმნა (avatar), როდის შეიქმნა
	- უნდა იყოს გაფილტვრის შესაძლებლობა: თარიღის მიხედვით, კომენტარების რაოდენობით, ლაიქების რაოდენობით (ყველა შემთხვევაში უნდა იყოს ზრდადობა კლებადობის შესაძლებლობა)
	- უნდა იყოს სერჩი სადაც Title-ით მოძებნით პოსტს ან პოსტის body-ში შემავალი keyword-ით 
- უნდა შეგეძლოთ თითოეული იუზერის ფეიჯზე შესვლა და ნახვა რა პოსტები აქვთ, ასევე რომელი პოსტები აქვთ დალაიქებული
- Post-ის მფლობელს უნდა შეეძლოს თავისი (მხოლოდ თავისი) პოსტის Update/Delete ყველა ეს ქმედება.

### გაითვალისწინეთ
* დაულოგინებელ იუზერს არ უნდა შეეძლოს პოსტის შექმნა, მხოლოდ ნახვა
* ლოგინის/რეგისტრაციის ვიუზე შესვლა მხოლოდ დაულოგინებელ იუზერს უნდა შეეძლოს | ლოგაუთზე მხოლოდ დალოგინებულს
* იუზერებს ერთმანეთს პოსტების შეცვლა/წაშლა არ უნდა შეეძლოთ!

### Bonus
- დაამატეთ ლოგიკა, სადაც, იუზერებს შეეძლებათ დამეგობრება
- იუზერს შეეძლოს მხოლოდ კონკრეტულ მეგობრებს გაუზიაროს პოსტი
- იუზერს შეეძლოს შეზღუდოს კომენტარების დაწერა არა მეგობრებისთვის, მაგრამ ნახვა მაინც შეეძლოთ პოსტის


