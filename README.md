### Operability of Software

This is a demo application for learning about operability of software.

#### Setup

1. Fork this repository to your GitHub account
2. Clone it to your local machine.
3. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
4. Run `heroku login`
5. In the folder of the operability of software app, run `heroku create`
6. Push your app to Heroku by doing `git push heroku master`
7. Once the push finishes, run `heroku open` to see your app
8. Reload the frontpage a few times, you should eventually see an error!

#### Sentry

Add Sentry to your application.

In the `operability_of_software` folder run: `heroku addons:create sentry`

You should get an email with a link to confirm your email, click that.

To open Sentry, run: `heroku addons:open sentry`

Can you see the error in your application?
What is the name of the exception?
What is the message accompanied with the exception?
What is the IP of the user who triggered the exception?
Can you see what browser and OS they (you) are using?
Can you see the filename and line number where the error occured?
Can you view the stack trace for the error?
Can you see how many times the error has occured?

#### NewRelic

Add NewRelic to your application.

```
heroku addons:create newrelic
heroku restart
```

Reload the front page of your app a few times. It can take a few minutes for
data to appear in your dashboard. Then open NewRelic by running
`heroku addons:open newrelic`.

You should see a list of applications, click on `production`. This shows you
a lot of information, have a look around.

Can you see the error rate of the application?
Can you see the average response time?
Can you see the requests per minute?
Can you see the CPU and memory usage of the server?

Alerts are sadly not available in the free version of NewRelic, but we could
create alerts around these metrics hitting certain thresholds. Click the
"alerts" in the top menu to see more information.

#### Papertrail

Add Papertrail to your application by running `heroku addons:create papertrail`.

It will take five minutes or so until logs start appearing in Papertrail.

Once a little while as passed, you can view Papertrail logs by running
`heroku addons:open papertrail`.

The log file is mostly a list of HTTP requests coming in, each request triggers
some stuff being added to the log file. Reload the page and see the information
being added to the log file.

Have a read through a part of the file and see what information is there.

There is some debugging information about the error in the logs, can you find
it? It should tell you the chance of the front page raising an error.
Can you see the name of the controller being accessed one the root path?
Can you see the name of the view being rendered?
Can you see the HTTP code being returned?

Note: you can always use the default Heroku method to view logs by running
`heroku logs`.

#### Deleting your Application

Once you're done, you might want to delete your application.

```
heroku destroy
```
