# Foodie
Foodie is a food blog, it is for anyone who loves food, cooking and sharing recipes or who would like to learn to cook.
Foodie users can register for an account which gives them some added perks. Users without an account can still access the blog and read posts, they can’t interact with them. Users can contact the blog director through social media which is linked in the footer.

[Link to live project](https://my-foodie-blog-c16c6ec88ef7.herokuapp.com//)

![screenshot of the landing page](/media/images/Screenshot%20(54).png)

### features:
* Navigation
    * The navigation bar is situated at the top of each page and contains the website logo which links to the home page.
    * The navigation bar also contains links to the home, contacts and my profile(dropdown menu). The dropdown menu changes based on whether a user is logged in or not.
    * If the user is not logged in my profile contains a register and login. Once the user is logged in my profile contains : my posts, make post, add category, edit profile, logout
    * The navigation bar gives the user easy access to each part of the website, on all devices.

![screenshot of the navbar when logged out](/media/images/Screenshot%20(56).png)

![screenshot of the navbar when logged in](/media/images/Screenshot%20(55).png)

* Landing page
    * The landing page contains all of the posts. Each post contains a picture or placeholder image, followed by a title ,an excerpt, the difficulty level of the recipe, a read more button and the post's author.
    * the landing page gives the user summary information about each post.

![screenshot of the landing page](/media/images/Screenshot%20(52).png)

* Post detail page
    * The page shows the post's title followed by the category name which  is a link to that category page.
    * Under the title there’s the author and the date of the post.
    * If you are the author of the post you will be able to see an update and a delete button.
    * At the bottom of the post the user can find a like button, a comment section and a back button.

![screenshot of the post when the user is not the author](/media/images/Screenshot%20(57).png)
![screenshot of the post when the user is the author](/media/images/Screenshot%20(59).png)
![screenshot of like button and comment section](/media/images/Screenshot%20(58).png)

* Register
    * It allows the user to sign up to Foodie and become a member.
    * The user will be asked to provide their username, first name, last name, email address and password.
    * The registration form gives the user the chance to join Foodie and become an official member with added benefits(liking, commenting, posting and adding categories).

![screenshot of the registration form](/media/images/Screenshot%20(60).png)

* Login
    * It allows the user to login to Foodie and access their profile.
    * Once the user has logged in, the user has access to my posts page, make post page, edit profile page, add category page.
![screenshot of the login form](/media/images/Screenshot%20(61).png)

* Edit profile
    * It allows the user to edit their Foodie profile via a prepopulated form.
    * The User can change their username, firstname, surname and password.

![screenshot of the edit profile form](/media/images/Screenshot%20(62).png)

* Create post
    * It allows the user to create a post. Each post can contain a title, author, excerpt, category, difficulty, body and image.

![screenshot of the make post page](/media/images/Screenshot%20(63).png)

* Update post
    * It allows the user to update a post of theirs via a prepopulated form. Any field of the post can be updated except for the author which is set by default.

![screenshot of the update post page](/media/images/Screenshot%20(64).png)

* Delete post
    * It allows a user to delete a post.

![screenshot of the delete post page](/media/images/Screenshot%20(65).png)

* Add category
    * Allows you to add a category if the ones present don't align with your post. 
    * Other users will be able to add posts to your category as well. 

![screenshot of the add category page](/media/images/Screenshot%20(66).png)

* Category page
    * Each post has a category which is on the post detail page next to the title. If the category is clicked the user is redirected to a page where other posts belonging to that category can be found.

![screenshot of the category page](/media/images/Screenshot%20(67).png)

* Footer
    * The footer is situated at the very bottom of each web page and contains links to Foodie’s social media accounts (Facebook, Twitter, Instagram and Youtube), these links will open in separate pages.
    * It allows the user to contact Foodie directly.

![screenshot of the category page](/media/images/Screenshot%20(68).png)


### testing:

| Action | Expected behaviour | Pass or Fail |
|---|---|---|
| Enter URL in browser | the landing page of the website should display on the screen | Pass |
| Click Home on the navigation bar | the home page should show up on the screen | Pass |
| Click Logo on the navigation bar | the home page should show up on the screen | Pass |
| Click Contact on the navigation bar| the social media links in the footer should show up on the screen | Pass |
| Click my profile (not logged in) on the navigation bar | A dropdown menu should appear containing ‘register’ and ‘login’. | Pass |
| Click my profile (logged in) on the navigation bar | A dropdown menu should appear containing ‘my posts’, ‘make post’, ‘add category’, ‘edit profile’, ‘logout’| Pass |
| Click Register in the dropdown menu | You should be redirected to a registration form | Pass |
| Click Login in the dropdown menu | You should be redirected to a login form | Pass |
| Click My posts in the dropdown menu | A page containing all of the user’s posts should appear | Pass |
| Click Make post in the dropdown menu | A form containing six fields (title, excerpt, category, difficulty, body and image) should appear | Pass |
| Click Add category in the dropdown menu | A form containing a field (category) should appear | Pass |
| Click Edit profile the dropdown menu | A form containing four fields (username, first name, last name and email) and a link to the password changing form should appear | Pass |
| Click Logout in the dropdown menu | the user should be redirected to the home page | Pass |
| Click the ‘read more’ button on a post | The post detail page should appear | Pass |
| Click the category link  next to the post title | A page with other posts belonging to that category should appear | pass |
| Click the edit button underneath  the post title | The user should be redirected to the update post page | pass |
| Click the delete button underneath the post title | The user should be redirected to the delete post page | pass |
| Click the like button under the post body | A like should be added to the count and the should be black. If you click again the count should go down and the like button should go from black to white | pass |
| Click the ‘add one’  link  in the comment section | A comment  form containing 2 fields (name, body) | pass |
| Click the back button at the end of the post | Takes the user back to the home page | pass |



