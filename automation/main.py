import json 
import math


def save(html, filename):
    f_write = open(filename, "w")
    f_write.write(html)
    f_write.close()


# Opening JSON file
f = open('database.json')
  
data = json.load(f)


# testimonials
var_testimonial = ""
for testimonial in data['testimonials']:
    var_testimonial = var_testimonial + '''
    <article class="quote quote-creative">
        <div class="media media-xs flex-column flex-xs-row-reverse">
            <div class="media-left">
                <div class="quote-author-figure">
                    <div class="quote-author-image-decor"></div>
                    <img class="quote-author-image rounded-circle" src="''' + str(testimonial['image']) + '''" alt="" width="64"
                        height="64" loading="lazy" />
                </div>
            </div>
            <div class="media-body">
                <div class="quote-author-name h5" style="text-align: left;">''' + str(testimonial['name']) + '''</div>
                <div class="quote-text" style="text-align: justify;">'''    
    for _, breaker in enumerate(testimonial['content']):
        if _ == len(testimonial['content']) - 1:
            var_testimonial = var_testimonial + str(breaker)
        else:
            var_testimonial = var_testimonial + str(breaker) + '<br>'
    end_code1 = '''</div>
                <div class="quote-author-company" style="text-align: left;">'''
    var_testimonial = var_testimonial + end_code1
    for _, breaker in enumerate(testimonial['designation']):
        if _ == len(testimonial['designation']) - 1:
            var_testimonial = var_testimonial + str(breaker)
        else:
            var_testimonial = var_testimonial + str(breaker) + '<br>'           
    end_code2 = '''
                </div>
            </div>
        </div>
    </article>
    '''
    var_testimonial = var_testimonial + end_code2


# badges
var_badge = ""
for badge in data['badges']:
    var_badge = var_badge + '''
    <article class="pricing pricing-primary block block-sm block-center" data-animate='{"class":"fadeInUp"}'>
              <div class="pricing-body">
                <a href="''' + str(badge['img']) + '''" target="_blank"><img
                    src="''' + str(badge['img']) + '''" alt="" width="100%" height="100%"
                    loading="lazy"></a>
                <div class="pricing-divider">
                  <hr class="divider">
                </div>
                <div class="pricing-btn">
                  <center><b>''' + str(badge['name']) + '''</b></center>
                  ''' + str(badge['desc']) + '''<br>''' + str(badge['date']) + '''
                </div>
              </div>
            </article>
    '''


# certificates
var_certificate = ""
for certificates in data['certificates']:
    var_certificate = var_certificate + '''
    <article class="pricing pricing-primary block block-sm block-center" data-animate='{"class":"fadeInUp"}'>
              <div class="pricing-body">
                <a href="''' + str(certificates['img']) + '''" target="_blank"><img
                    src="''' + str(certificates['img']) + '''" alt="" width="100%" height="100%"
                    loading="lazy"></a>
                <div class="pricing-divider">
                  <hr class="divider">
                </div>
                <div class="pricing-btn">
                  <center><b>''' + str(certificates['name']) + '''</b></center>
                  ''' + str(certificates['desc']) + '''<br>''' + str(certificates['date']) + '''
                </div>
              </div>
            </article>
    '''


# partners
var_partners = ""
for ind, partner in enumerate(data['partners']):
    var_partners = var_partners + '''
     <div class="col-4 col-sm-3 partner-group-item"><a class="partner" aria-label="collab" id="removeHref'''+ str(ind+1) +'''"
              href="https://www.abhijithudayakumar.com/" onclick="removeLink(this.id);" style="cursor: default;">
              <img class="partner-image" src="'''+ str(partner['img']) +'''" alt="" width="600" height="180"
                loading="lazy" />
            </a></div>
    '''


# popular projects
var_work = ""
for work in data['works']:
    if work['H_visible']:
        var_header = ""
        if work['header']:
          var_header = '''<div class="pricing-badge">'''+ str(work['header']) +'''</div>'''
        var_scope = '''<button class="btn btn-sm" onclick='window.open("''' + str(work['repo']) + '''");'>See Repo</button>'''
        if work['Access'] == 1:
          var_scope = '''<button class="btn btn-sm" data-modal-trigger="{&quot;target&quot;:&quot;#modal&quot;}">See Repo</button>'''
        if work['category'] == "Websites":
          var_scope = '''<button class="btn btn-sm"
                                onclick='window.open("''' + str(work['link']) + '''");'>Visit Website</button><br>
                              <button class="btn btn-sm"
                                onclick='window.open("''' + str(work['repo']) + '''");'>See Repo</button>
                            '''
        var_work = var_work + '''
        <article class="pricing pricing-primary block block-sm block-center" data-animate='{"class":"fadeInUp"}'>
                '''+ var_header +'''<div class="pricing-body">
                    <div class="pricing-title biggest h2">''' + str(work['name']) + '''</div>
                    <img src="''' + str(work['logo']) + '''" alt="''' + str(work['category']) + '''" width="100%" height="100%" loading="lazy">
                    <div class="pricing-divider">
                    <hr class="divider">
                    </div>
                    <div class="pricing-list pricing-year">

                    <ul class="list list-marked-check d-inline-block text-left">
                        <li class="list-item">Contributors : ''' + str(work['contributors']) + '''</li>
                        <li class="list-item">Issues : ''' + str(work['issues']) + '''</li>
                        <li class="list-item">Stars : ''' + str(work['stars']) + '''</li>
                        <li class="list-item">Forks : ''' + str(work['forks']) + '''</li>
                        <li class="list-item disabled">Description : ''' + str(work['desc']) + '''</li>
                    </ul>
                    </div>
                    <div class="pricing-btn">
                    '''+var_scope+'''
                    </div>
                </div>
                </article>
        '''


code_homepage = '''
<!DOCTYPE html>
<html lang="en">

<head>

  <title>Abhijith Udayakumar | Portfolio - Home</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <!-- <script src="components/cdn/3ts2ksMwXvKRuG480KNifJ2_JNM.js"></script> -->
  <link rel="preconnect" as="image" href="media/favicon.ico" />
  <link rel="icon" href="media/favicon.ico" type="image/x-icon">

  <link rel="preload" as="style" href="components/base/base-2.css">
  <!-- <link rel="preload" href="components/mdi/mdi.woff2" as="font"> -->
  <link rel="preload" as="script" href="components/base/core.min.js" />
  <link rel="preload" as="script" href="components/base/script.js" />

  <link rel="stylesheet" href="components/base/base-2.css">
  <script src="components/base/core.min.js"></script>
  <script src="components/base/script.js"></script>

  <!-- <script type="text/javascript" src="database.json"></script> -->
  <script type="text/javascript" src="db.js"></script>


  <meta name="title" content="Abhijith Udayakumar | Portfolio">
  <meta name="description" content="Abhijith Udayakumar's Portfolio Website">
  <!-- <meta name="robots" content="noindex,nofollow"> -->
  <link rel="canonical" href="https://www.abhijithudayakumar.com">
  <meta name="twitter:url" property="og:url" content="https://www.abhijithudayakumar.com">

  <meta name="twitter:card" content="summary" />
  <meta name="twitter:site" content="@AbhijithUdayakumar" />
  <meta name="twitter:title" content="Abhijith Udayakumar | Portfolio" />
  <meta name="twitter:description" content="Abhijith Udayakumar's Portfolio Website" />
  <meta name="twitter:image" content="https://www.abhijithudayakumar.com/media/assets/welcome-400x400.png" />
  <meta name="twitter:creator" content="@'''+ data['social']['Twitter'] +'''">

  <meta property="go:url" content="https://www.abhijithudayakumar.com" />
  <meta property="go:type" content="website" />
  <meta property="og:title" content="Portfolio" />
  <meta property="go:description" content="Abhijith Udayakumar's Portfolio Website" />
  <meta property="og:image" content="https://www.abhijithudayakumar.com/media/assets/welcome-400x400.png" />
  <meta property="og:site_name" content="Abhijith Udayakumar | Portfolio">

</head>

<body>
  <div class="page">
    <!--RD Navbar-->
    <header class="section rd-navbar-wrap">
      <nav class="rd-navbar context">
        <div class="navbar-container">
          <div class="navbar-cell">
            <div class="navbar-panel">
              <button class="navbar-switch"
                data-multi-switch='{"targets":".rd-navbar","scope":".rd-navbar","isolate":"[data-multi-switch]"}'></button>
              <div class="navbar-logo"><a class="navbar-logo-link" href="https://www.abhijithudayakumar.com"><img
                    class="navbar-logo-inverse" src="media/logo1.svg" alt="Logo" width="300" height="30"
                    loading="lazy" /></a></div>
            </div>
          </div>
          <div class="navbar-spacer"></div>
          <div class="navbar-cell navbar-sidebar">
            <ul class="navbar-navigation rd-navbar-nav fullpage-navigation">
              <li class="navbar-navigation-root-item active" data-menuanchor="home"><a
                  class="navbar-navigation-root-link" href="#home">Home</a>
              </li>
              <li class="navbar-navigation-root-item" data-menuanchor="about"><a class="navbar-navigation-root-link"
                  href="#about">About Me</a>
              </li>
              <li class="navbar-navigation-root-item" data-menuanchor="work"><a class="navbar-navigation-root-link"
                  href="#work">My Works</a>
              </li>
              <!-- <li class="navbar-navigation-root-item" data-menuanchor="work"><a class="navbar-navigation-root-link" href="#certificates">My Achievements</a>
                </li> -->
              <li class="navbar-navigation-root-item" data-menuanchor="blog"><a class="navbar-navigation-root-link"
                  href="'''+ data['social']['blog'] +'''" target="_blank" rel="noopener">Blog</a>
              </li>
              <li class="navbar-navigation-root-item" data-menuanchor="contacts"><a class="navbar-navigation-root-link"
                  href="#contacts">Contact Me</a>
              </li>
            </ul>
          </div>
          <div class="navbar-cell">
            <div class="navbar-subpanel">
              <div class="navbar-subpanel-item">
                <button class="navbar-button navbar-info-button mdi-dots-vertical"
                  data-multi-switch='{"targets":".rd-navbar","scope":".rd-navbar","class":"navbar-info-active","isolate":"[data-multi-switch]"}'></button>
                <div class="navbar-info">
                  <button class="btn btn-sm"
                    onclick='window.location.href="'''+ data['social']['Resume'] +'''";'>Get
                    My Resume</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </header>
    <!-- Intro-->
    <section class="section" id="home">
      <div class="swiper-container swiper-pagination-minimal"
        data-swiper='{"scrollbar":{"el":""},"autoplay":{"delay":5000,"disableOnInteraction":false},"breakpoints":{"320":{"autoplay":false},"1200":{"autoplay":{"delay":5000,"disableOnInteraction":false}}}}'>
        <div class="bg-layer d-flex align-items-end">
          <svg class="image-svg" width="1920" height="792" viewBox="0 0 1920 792" fill="none">
            <!-- <path d="M155.44 227.32H227.26V523H155.44L35.32 336.94V523H-36.5V227.32H35.32L155.44 413.38V227.32ZM389.935 525.94C355.775 525.94 327.775 515.02 305.935 493.18C284.095 471.06 273.175 441.8 273.175 405.4C273.175 369 283.955 340.02 305.515 318.46C327.355 296.9 355.495 286.12 389.935 286.12C424.375 286.12 452.935 296.76 475.615 318.04C498.295 339.32 509.635 368.86 509.635 406.66C509.635 414.78 509.075 422.34 507.955 429.34H346.675C348.075 439.7 352.695 448.24 360.535 454.96C368.375 461.4 376.775 464.62 385.735 464.62C394.975 464.62 401.835 463.78 406.315 462.1C410.795 460.14 414.015 458.32 415.975 456.64C418.215 454.68 421.015 451.6 424.375 447.4H502.075C495.355 470.92 481.915 489.96 461.755 504.52C441.595 518.8 417.655 525.94 389.935 525.94ZM434.875 384.4C433.755 373.48 428.995 364.66 420.595 357.94C412.195 350.94 402.255 347.44 390.775 347.44C379.295 347.44 369.635 350.94 361.795 357.94C353.955 364.66 349.055 373.48 347.095 384.4H434.875ZM696.466 449.5C705.986 439.42 710.746 424.86 710.746 405.82C710.746 386.78 705.846 372.36 696.046 362.56C686.246 352.48 674.626 347.44 661.186 347.44C647.746 347.44 636.126 352.48 626.326 362.56C616.806 372.36 612.046 386.78 612.046 405.82C612.046 424.86 616.946 439.42 626.746 449.5C636.826 459.58 648.586 464.62 662.026 464.62C675.466 464.62 686.946 459.58 696.466 449.5ZM574.246 492.76C550.726 470.64 538.966 441.52 538.966 405.4C538.966 369.28 550.726 340.44 574.246 318.88C597.766 297.04 626.886 286.12 661.606 286.12C696.326 286.12 725.306 297.04 748.546 318.88C772.066 340.44 783.826 369.28 783.826 405.4C783.826 441.52 772.206 470.64 748.966 492.76C725.726 514.88 696.746 525.94 662.026 525.94C627.306 525.94 598.046 514.88 574.246 492.76ZM901.98 288.64V323.08C916.82 298.44 940.48 286.12 972.96 286.12C999.84 286.12 1021.54 295.08 1038.06 313C1054.86 330.92 1063.26 355.28 1063.26 386.08V523H991.86V395.74C991.86 380.62 987.8 369 979.68 360.88C971.84 352.48 960.92 348.28 946.92 348.28C932.92 348.28 921.86 352.48 913.74 360.88C905.9 369 901.98 380.62 901.98 395.74V523H830.16V288.64H901.98Z" fill="url(#paint0_linear)"></path> -->
            <path
              d="M1245 671.5H0V792H1920V0.5H1450C1392.01 0.5 1345 47.5101 1345 105.5V571.5C1345 626.728 1300.23 671.5 1245 671.5Z"
              fill="#DEEBF7"></path>
            <circle cx="509" cy="121" r="18" fill="#D1E4F4"></circle>
            <circle cx="367.5" cy="138.5" r="9.5" fill="#FF8C68"></circle>
            <!-- <circle cx="526.5" cy="431.5" r="6.5" fill="#78C5D6"></circle> -->
            <defs>
              <lineargradient id="paint0_linear" x1="-30.2098" y1="414" x2="1076.2" y2="412.898"
                gradientUnits="userSpaceOnUse">
                <stop offset="0" stop-color="#DEEBF6" stop-opacity="0.49"></stop>
                <stop offset="1" stop-color="#DEEBF6"></stop>
              </lineargradient>
            </defs>
          </svg>
        </div>
        <div class="swiper-wrapper">
          <div class="swiper-slide section-lg">
            <div class="container">
              <div class="row align-items-center justify-content-lg-between flex-md-row-reverse">
                <div class="col-8 col-md-6"><img src="media/home-1-s.png" alt="" width="1000" height="769"
                    loading="lazy" />
                </div>
                <div class="col-md-7 col-lg-6">
                  <h1>Hello There !!</h1>
                  <div class="offset-xxs">
                    <p class="biggest">Introduce = { <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Name" :
                      "Abhijith Udayakumar",
                      <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Location" : "Earth",
                      <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Proficiency" : ['Python', 'ML', 'Data
                      Analysis']
                      <br>}
                    </p>
                  </div>
                  <!-- <div class="offset-sm">
                      <a class="btn btn-app pl-1" href="https://github.com/Abhijith14/SnakeGame-ML" target="_blank" rel="noopener">
                        <span class="btn-icon icon icon-round icon-sm icon-primary icon-style-3 mdi-github-circle"></span>
                        <span>View on Github</span>
                      </a>
                    </div> -->
                </div>
              </div>
            </div>
          </div>
          <div class="swiper-slide section-lg">
            <div class="container">
              <div class="row align-items-center justify-content-lg-between flex-md-row-reverse">
                <div class="col-8 col-md-6"><img src="media/home-2-s.png" alt="" width="1000" height="769"
                    loading="lazy" />
                </div>
                <div class="col-md-7 col-lg-6">
                  <h1>Hello There !!</h1>
                  <div class="offset-xxs">
                    <p class="biggest">Introduce = { <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Name" :
                      "Abhijith Udayakumar",
                      <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Location" : "Earth",
                      <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Proficiency" : ['Python', 'ML', 'Data
                      Analysis']
                      <br>}
                    </p>
                  </div>
                  <!-- <div class="offset-sm">
                      <a class="btn btn-app pl-1" href="https://github.com/Abhijith14/discord-bot" target="_blank" rel="noopener">
                        <span class="btn-icon icon icon-round icon-sm icon-primary icon-style-3 mdi-github-circle"></span>
                        <span>View on Github</span>
                      </a>
                    </div> -->
                </div>
              </div>
            </div>
          </div>
          <div class="swiper-slide section-lg">
            <div class="container">
              <div class="row align-items-center justify-content-md-between flex-md-row-reverse">
                <div class="col-8 col-md-6"><img src="media/home-3-s.png" alt="" width="1000" height="769"
                    loading="lazy" />
                </div>
                <div class="col-md-7 col-lg-6">
                  <h1>Hello There !!</h1>
                  <div class="offset-xxs">
                    <p class="biggest">Introduce = { <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Name" :
                      "Abhijith Udayakumar",
                      <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Location" : "Earth",
                      <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Proficiency" : ['Python', 'ML', 'Data
                      Analysis']
                      <br>}
                    </p>
                  </div>
                  <!-- <div class="offset-sm">
                      <a class="btn btn-app pl-1" href="https://github.com/Abhijith14/VB.NET-PROJECTS" target="_blank" rel="noopener">
                        <span class="btn-icon icon icon-round icon-sm icon-primary icon-style-3 mdi-github-circle"></span>
                        <span>View on Github</span>
                      </a>
                    </div> -->
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="swiper-pagination" data-pagination-ordered></div>
      </div>
    </section>
    <!-- Features-->
    <section class="section section-lg bg-transparent" id="about">
      <div class="container">
        <div class="row row-30 gutters-xxl-60">
          <div class="col-md-3">
            <!-- Blurb boxed-->
            <article class="blurb blurb-boxed">
              <div class="media media-sm flex-column">
                <div class="media-left">
                  <div class="blurb-embed"><span
                      class="icon icon-round icon-md icon-secondary icon-style-3 mdi-github-box"></span></div>
                </div>
                <div class="media-body">
                  <div class="blurb-title h5"><span data-toggle="tooltip" data-placement="top" title=""
                      data-original-title="Visit GitHub" style="cursor: pointer;"
                      onclick='window.open("'''+ data['social']['Github'] +'''", "_blank");'>GitHub Profile</span></div>
                  <div class="blurb-text">Visit my GitHub profile to learn more about my coding projects.</div>
                </div>
              </div>
            </article>
          </div>
          <div class="col-md-3">
            <!-- Blurb boxed-->
            <article class="blurb blurb-boxed">
              <div class="media media-sm flex-column">
                <div class="media-left">
                  <div class="blurb-embed"><span class="icon icon-round icon-md icon-primary icon-style-3"><img
                        src="media/logo-kaggle.png" width="24px" height="24px" alt="kaggle" loading="lazy"></span></div>
                </div>
                <div class="media-body">
                  <div class="blurb-title h5"><span data-toggle="tooltip" data-placement="top" title=""
                      data-original-title="Visit Kaggle" style="cursor: pointer;"
                      onclick='window.open("'''+ data['social']['Kaggle'] +'''", "_blank");'>Kaggle
                      Profile</span></div>
                  <div class="blurb-text">Get to know more about my Machine Learning and Data Visualisation skills.
                  </div>
                </div>
              </div>
            </article>
          </div>
          <div class="col-md-3">
            <!-- Blurb boxed-->
            <article class="blurb blurb-boxed">
              <div class="media media-sm flex-column">
                <div class="media-left">
                  <div class="blurb-embed"><span
                      class="icon icon-round icon-md icon-success icon-style-3 mdi-linkedin-box"></span></div>
                </div>
                <div class="media-body">
                  <div class="blurb-title h5"><span data-toggle="tooltip" data-placement="top" title=""
                      data-original-title="Visit LinkedIn" style="cursor: pointer;"
                      onclick='window.open("'''+ data['social']['LinkedIn'] +'''", "_blank");'>LinkedIn</span>
                  </div>
                  <div class="blurb-text">Connect with me @LinkedIn to know about my achievements and current work
                    profile.</div>
                </div>
              </div>
            </article>
          </div>
          <div class="col-md-3">
            <!-- Blurb boxed-->
            <article class="blurb blurb-boxed">
              <div class="media media-sm flex-column">
                <div class="media-left">
                  <div class="blurb-embed"><span class="icon icon-round icon-md icon-primary icon-style-3"><img
                        src="media/buddydev.png" width="24px" height="24px" alt="buddy" loading="lazy"></span></div>
                </div>
                <div class="media-body">
                  <div class="blurb-title h5"><span data-toggle="tooltip" data-placement="top" title=""
                      data-original-title="Visit BUDDY Developer" style="cursor: pointer;"
                      onclick="window.open('https://www.createwithbuddy.tech', '_blank');">Create With BUDDY</span>
                  </div>
                  <div class="blurb-text">Visit BUDDY Developer to get to know about my Startup and its accomplishments
                  </div>
                </div>
              </div>
            </article>
          </div>
        </div>
      </div>
    </section>
    <!-- Features-->
    <section class="section section-md bg-transparent">
      <div class="container">
        <div class="swiper-modern-wrap">
          <div class="swiper-container swiper-modern"
            data-swiper='{"loop":false,"autoplay":false,"simulateTouch":false,"slidesPerView":1,"spaceBetween":30,"pagination":{"el":""},"scrollbar":{"draggable":true}}'>
            <div class="swiper-wrapper">
              <div class="swiper-slide">
                <div class="row row-10 align-items-center">
                  <div class="col-10 col-sm-8 col-lg-6 col-xxl-7"><img src="media/home-4-01-734x564.png" alt=""
                      width="734" height="564" loading="lazy" />
                  </div>
                  <div class="col-lg-6 col-xxl-5">
                    <div class="title-icon group-20 mt-xxl-2"><span
                        class="icon icon-circle icon-lg icon-style-4 mdi-cursor-default"></span>
                      <h2>Hello W.O.R.L.D !!</h2>
                    </div>
                    <p class="bigger">My name is <b>Abhijith Udayakumar</b> and I'm a Machine-learning enthusiast and
                      Python Developer. I'm from India, living in Kerala and currently working as CEO of <span
                        class="text-dark" data-toggle="tooltip" data-placement="top" title=""
                        data-original-title="Visit BUDDY Developer" style="cursor: pointer;"
                        onclick="window.open('https://www.createwithbuddy.tech', '_blank');"><b>BUDDY
                          Developer</b></span>, Technical & Operation Support Officer at <span class="text-dark"
                        data-toggle="tooltip" data-placement="top" title="" data-original-title="Visit GADS Solutions"
                        style="cursor: pointer;"
                        onclick="window.open('https://www.gadssolutions.in/', '_blank');"><b>GADS</b></span> (Geeks At
                      Designing Solutions) and Head of Media-Reach team in <span class="text-dark" data-toggle="tooltip"
                        data-placement="top" title="" data-original-title="Visit LiveWires_ Club"
                        style="cursor: pointer;"
                        onclick="window.open('https://live-wires.herokuapp.com/', '_blank');"><b>LiveWires_ Student
                          Club</b></span> SRMIST.</p><!-- <a class="btn" href="#">Start Using for Free</a> -->
                  </div>
                </div>
              </div>
              <div class="swiper-slide">
                <div class="row row-10 align-items-center">
                  <div class="col-10 col-sm-8 col-lg-6 col-xxl-7"><img src="media/buddyai.png" alt="" width="734"
                      height="564" loading="lazy" />
                  </div>
                  <div class="col-lg-6 col-xxl-5">
                    <div class="title-icon group-20 mt-xxl-2"><span
                        class="icon icon-circle icon-lg icon-style-4 mdi-settings"></span>
                      <h2>BUDDY AI</h2>
                    </div>
                    <p class="bigger">Intelligence is never Aritificial. Bringing my passion out alive I developed BUDDY
                      AI as my companion to my daily life. This artificially intelligent bot helps me in all my digital
                      work.</p><a class="btn" id="removeHref" href="https://www.abhijithudayakumar.com/"
                      onclick="removeLink(this.id);" data-modal-trigger='{"target":"#modal"}'
                      style="color: white;">Request a demo</a>
                  </div>
                </div>
              </div>
              <div class="swiper-slide">
                <div class="row row-10 align-items-center">
                  <div class="col-10 col-sm-8 col-lg-6 col-xxl-7"><img src="media/home-4-02-606x564.png" alt=""
                      width="606" height="564" loading="lazy" />
                  </div>
                  <div class="col-lg-6 col-xxl-5">
                    <div class="title-icon group-20 mt-xxl-2"><span
                        class="icon icon-circle icon-lg icon-style-4 mdi-settings"></span>
                      <h2>Create With BUDDY</h2>
                    </div>
                    <p class="bigger">Problems are undoubtedly the definite part of our life and solutions are what we
                      need to seek & merge with it .To simplify your search we welcome you to BUDDY where we bring to
                      you hammers to break all the technical trouble heads that pops up while you work, learn or enjoy.
                    </p><a class="btn" href="https://createwithbuddy.tech" target="_blank" rel="noopener">Visit BUDDY
                      Developer</a>
                  </div>
                </div>
              </div>
            </div>
            <div class="swiper-scrollbar"></div>
          </div>
        </div>
      </div>
    </section>
    <section class="section section-xl position-relative" id="work">
      <div class="bg-layer-2">
        <svg class="image-svg" width="1920" height="792" viewBox="0 0 1920 792" fill="none">
          <path
            d="M615 120.5L1920 120.5L1920 0.000183105L0.000295939 1.52537e-05L0.000244141 592.5L410 592.5C467.99 592.5 515 545.49 515 487.5L515 220.5C515 165.272 559.772 120.5 615 120.5Z"
            fill="#DEEBF7"></path>
        </svg>
      </div>
      <div class="container position-relative">
        <div class="group-20 d-sm-flex align-items-sm-end justify-content-sm-between text-center">
          <h2>My Works</h2>
          <div>
            <!-- Multi switch-->
            <div class="switch-text group-25 d-inline-flex align-items-center justify-content-center" id="multiswitch">
              <div><span class="switch-text-left biggest">Detailed View</span><span
                  class="switch-text-right biggest ml-2 border-left pl-2">Normal View</span></div>
              <div class="switch-toggle-modern"
                data-multi-switch='{"targets":"#multiswitch, #pricing-group","state":true}'>
                <div class="guide"></div>
                <div class="slider">
                  <div class="slider-dot"></div>
                  <div class="slider-dot"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="pricing-group offset-xs" id="pricing-group">
          <!-- Owl Carousel-->
          <div class="owl-carousel owl-style-1 owl-item-end"
            data-owl="{&quot;loop&quot;:false,&quot;mouseDrag&quot;:false,&quot;dots&quot;:true,&quot;autoplay&quot;:false,&quot;responsive&quot;:{&quot;768&quot;:{&quot;items&quot;:2},&quot;992&quot;:{&quot;items&quot;:3},&quot;1600&quot;:{&quot;items&quot;:3,&quot;margin&quot;:90}}}">
            '''+var_work+'''
          </div>
        </div>
      </div>

      <!-- Modal-->
      <div class="modal fade" id="modal" tabindex="-1" role="dialog">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-body text-center">
              <h4>Request for <br>Repo Access</h4>
              <!--RD Mailform-->
              <form class="rd-mailform" data-form-output="modal-form-output-global" data-form-type="contact"
                method="post" action="components/rd-mailform/rd-mailform.php">
                <div class="form-group">
                  <input class="form-control" type="text" name="name" placeholder="Your name *"
                    data-constraints="@Required">
                </div>
                <div class="form-group">
                  <input class="form-control" type="email" name="email" placeholder="Your E-mail *"
                    data-constraints="@Email @Required">
                </div>
                <div class="offset-xs">
                  <button class="btn btn-block" type="submit">Send Request</button>
                </div>
                <br>
                <span>This repo has private scope.</span>
              </form>
            </div>
            <button class="close" type="button" data-dismiss="modal" aria-label="Close"><span
                aria-hidden="true">×</span></button>
          </div>
        </div>
      </div>

      <div class="form-output snackbar snackbar-secondary" id="modal-form-output-global"></div>
      <br>
      <br>
      <center>
        <button class="btn" onclick="window.location.href='work.html';">View All My Works</button>
      </center>
    </section>



    <!-- Badges -->
    <section class="section section-xl position-relative" id="certificates">
      <svg class="image-svg image-svg-1 position-absolute d-none d-xl-block" width="1920" height="418"
        viewBox="0 0 1920 418" fill="none">
        <path
          d="M-10 77.1127C73.5216 223.941 358.342 431.331 485.013 416.219C611.685 401.106 670.151 293.544 812 287.5C953.849 281.456 1017 437.5 1173.5 394.5C1330 351.5 1379 47.5 1920 0.5"
          stroke="#CBD7E6"></path>
      </svg>
      <div class="container position-relative">
        <div class="group-20 d-sm-flex align-items-sm-end justify-content-sm-between text-center">
          <h2>Badges Earned !!</h2>
        </div>
        <div class="pricing-group offset-xs" id="pricing-group">
          <!-- Owl Carousel-->
          <div class="owl-carousel owl-style-1 owl-item-end"
            data-owl="{&quot;loop&quot;:false,&quot;mouseDrag&quot;:false,&quot;dots&quot;:true,&quot;autoplay&quot;:false,&quot;responsive&quot;:{&quot;768&quot;:{&quot;items&quot;:2},&quot;992&quot;:{&quot;items&quot;:3},&quot;1600&quot;:{&quot;items&quot;:3,&quot;margin&quot;:90}}}">


            ''' + var_badge + '''


          </div>
        </div>
        <!--      	<br>-->
        <!--      	<center>-->
        <!--         	<button class="btn">View All My Achievements</button>-->
        <!--</center>-->
      </div>


    </section>



    <!-- Certificates-->
    <section class="section section-xl position-relative" id="certificates">
      <svg class="image-svg image-svg-1 position-absolute d-none d-xl-block" width="1920" height="418"
        viewBox="0 0 1920 418" fill="none">
        <path
          d="M-10 77.1127C73.5216 223.941 358.342 431.331 485.013 416.219C611.685 401.106 670.151 293.544 812 287.5C953.849 281.456 1017 437.5 1173.5 394.5C1330 351.5 1379 47.5 1920 0.5"
          stroke="#CBD7E6"></path>
      </svg>
      <div class="container position-relative">
        <div class="group-20 d-sm-flex align-items-sm-end justify-content-sm-between text-center">
          <h2>My Achievements</h2>
        </div>
        <div class="pricing-group offset-xs" id="pricing-group">
          <!-- Owl Carousel-->
          <div class="owl-carousel owl-style-1 owl-item-end"
            data-owl="{&quot;loop&quot;:false,&quot;mouseDrag&quot;:false,&quot;dots&quot;:true,&quot;autoplay&quot;:false,&quot;responsive&quot;:{&quot;768&quot;:{&quot;items&quot;:2},&quot;992&quot;:{&quot;items&quot;:3},&quot;1600&quot;:{&quot;items&quot;:3,&quot;margin&quot;:90}}}">

            ''' + var_certificate + '''
          </div>
        </div>
        <br>
        <center>
          <button class="btn">View All My Achievements</button>
        </center>
      </div>


    </section>

    <!-- What People Say-->
    <section class="section section-lg pt-0 section-one-screen">
      <div class="container">
        <h2 class="text-center">What People Say</h2>
        <div class="row row-offset-lg justify-content-center">
          <div class="col-xl-10">
            <div class="owl-carousel owl-style-1"
              data-owl="{&quot;dots&quot;:true,&quot;responsive&quot;:{&quot;768&quot;:{&quot;items&quot;:2}}}">
              <!-- Quote creative-->             
              '''+ var_testimonial +'''
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- Our partners-->
    <section class="section section-lg">
      <div class="container">
        <h2 class="text-center">My Partners</h2>
        <div class="row row-offset-xl no-gutters partner-group">
         '''+var_partners+'''
        </div>
      </div>
    </section>
    <!-- Get in touch-->
    <section class="section section-xl position-relative" id="contacts">
      <div class="bg-layer-2">
        <svg class="image-svg" width="1920" height="792" viewBox="0 0 1920 792" fill="none">
          <path
            d="M1305 120.5L-4.12635e-05 120.5L-5.1798e-05 6.10352e-05L1920 -0.000106817L1920 592.5L1510 592.5C1452.01 592.5 1405 545.49 1405 487.5L1405 220.5C1405 165.271 1360.23 120.5 1305 120.5Z"
            fill="#DEEBF7"></path>
        </svg>
      </div>
      <div class="container">
        <div class="row row-30 align-items-xl-center justify-content-xxl-between">
          <div class="col-lg-6">
            <h2>Get in Touch</h2>
            <p class="bigger op-6">Any query ,suggestion or collaboration-request. Don't hesitate to contact me directly
              using the form on this page or by visiting my GitHub profile.</p>
            <form class="rd-mailform mr-xxl-5" data-form-output="form-output-global" data-form-type="contact"
              method="post" action="cont.php">
              <div class="row row-30">
                <div class="col-xs-6">
                  <div class="form-group">
                    <input class="form-control" type="text" name="name" placeholder="Your name *"
                      data-constraints="@Required">
                  </div>
                </div>
                <div class="col-xs-6">
                  <div class="form-group">
                    <input class="form-control" type="email" name="email" placeholder="Your e-mail address *"
                      data-constraints="@Email @Required">
                  </div>
                </div>
                <div class="col-12">
                  <div class="form-group">
                    <textarea class="form-control" name="question" placeholder="Your question" rows="5"
                      data-constraints="@Required"></textarea>
                  </div>
                </div>
              </div>
              <div class="offset-sm group-40 d-flex flex-wrap flex-xs-nowrap align-items-center">
                <button class="btn" type="submit">Send Message</button>
                <!-- Checkbox-->
                <!-- <div class="custom-control custom-checkbox">
                          <input class="custom-control-input" type="checkbox" id="check1">
                          <label class="custom-control-label" for="check1">Get weekly news and updates
                          </label>
                        </div> -->
              </div>
            </form>
          </div>
          <div class="col-lg-6">
            <div class="box px-xl-3 px-xxl-4">
              <div class="row row-30">
                <div class="col-md-6 col-lg-12 col-xl-6">
                  <h4>Reference:</h4>
                  <div class="group-30 offset-sm">
                    <a class="btn btn-app pl-1" href="'''+ data['social']['Kaggle'] +'''" target="_blank"
                      rel="noopener">
                      <span class="btn-icon icon icon-round icon-sm icon-primary icon-style-3"><img
                          src="media/logo-kaggle.png" width="24px" height="24px" alt="kaggle" loading="lazy"></span>
                      <span>Kaggle.com</span>
                    </a>
                    <a class="btn btn-app pl-1" href="'''+ data['social']['Github'] +'''" target="_blank" rel="noopener">
                      <span class="btn-icon icon icon-round icon-sm icon-primary icon-style-3 mdi-github-box"></span>
                      <span>GitHub.com</span>
                    </a>
                  </div>
                </div>
                <div class="col-md-6 col-lg-12 col-xl-6">
                  <h4>Contacts:</h4>
                  <table class="table table-sm table-responsive-xl table-no-bordered bigger">
                    <tbody>
                      <tr>
                        <td class="text-right op-6 pl-0 align-middle">Ph.</td>
                        <td class="biggest"><a class="link-inherit" href="tel:919946883500">+91 9946883500</a></td>
                      </tr>
                      <tr>
                        <td class="text-right op-6 pl-0">Mail.</td>
                        <td>
                          <a class="link-inherit" href="mailto:abhijithukzm@gmail.com"
                            style="font-size: 14px;">abhijithukzm@gmail.com</a>
                          <br>
                          <a class="link-inherit" href="mailto:buddy.assistant14@gmail.com"
                            style="font-size: 14px;">buddy.assistant14@gmail.com</a>
                        </td>
                      </tr>
                      <!-- <tr>
                          <td class="text-right op-6 pl-0">Office.</td>
                          <td>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</td>
                        </tr> -->
                    </tbody>
                  </table>
                </div>
              </div>
              <hr class="divider">
              <div class="group-20 d-flex flex-wrap align-items-center justify-content-between">
                <div>
                  <!-- List social-->
                  <ul class="list list-social">
                    <li class="list-social-item"><a aria-label="social"
                        class="icon icon-circle icon-md icon-style-1 mdi-facebook"
                        href="'''+ data['social']['Facebook'] +'''" target="_blank" rel="noopener"></a></li>
                    <li class="list-social-item"><a aria-label="social"
                        class="icon icon-circle icon-md icon-style-1 mdi-twitter"
                        href="'''+ data['social']['Twitter'] +'''" target="_blank" rel="noopener"></a></li>
                    <li class="list-social-item"><a aria-label="social"
                        class="icon icon-circle icon-md icon-style-1 mdi-instagram"
                        href="'''+ data['social']['Instagram'] +'''" target="_blank" rel="noopener"></a></li>
                  </ul>
                </div>
                <div>
                  <!-- Copyright-->
                  <p class="rights bigger"><span>&copy; 2021.&nbsp;</span><span></span><span> All rights reserved</span>
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="form-output snackbar snackbar-secondary" id="form-output-global"></div>
    </section>
  </div>
  <!-- Modal-->
  <!-- <div class="modal fade" id="modal-login" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-body text-center">
            <h3>Log In</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing</p>
            <form class="rd-mailform">
              <div class="form-group">
                <input class="form-control" type="text" name="name" placeholder="Your name *" data-constraints="@Required">
              </div>
              <div class="form-group">
                <input class="form-control" type="password" name="password" placeholder="Password *" data-constraints="@Required">
              </div>
              <div class="offset-xxs group-40 d-flex flex-wrap flex-xs-nowrap align-items-center">
                <button class="btn btn-block" type="submit">Log in</button>
              </div>
            </form>
          </div>
          <button class="close" type="button" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
        </div>
      </div>
    </div> -->
  <!-- Preloader-->
  <div class="preloader">
    <div class="preloader-inner">
      <div class="preloader-dot"></div>
      <div class="preloader-dot"></div>
      <div class="preloader-dot"></div>
      <div class="preloader-dot"></div>
    </div>
  </div>

  <script type="text/javascript">

    function removeLink(id) {
      document.getElementById(id).removeAttribute('href');
    }
  </script>


</body>

</html>
'''


# =====================================================================================================================================



def mobile_view(category, position):
  pro_count = position
  mobile_body = '''<!-- mobile view -->'''
  for _, mobile_data in enumerate(data['works']):
    if _ >= position-1:
      if mobile_data['category'] == category:
        mobile_body = mobile_body + '''
                        <!-- Project ''' + str(pro_count) + ''' (in mobile) -->
                        <article class="pricing pricing-primary block block-sm block-center mobile-custom"
                          data-animate='{"class":"fadeInUp"}'>
                          <div class="pricing-body">
                            <div class="pricing-title biggest h2">''' + str(mobile_data['name']) + '''</div>
                            <img src="''' + str(mobile_data['logo']) + '''" loading="lazy">
                            <div class="pricing-divider">
                              <hr class="divider">
                            </div>
                            <div class="pricing-list pricing-year">

                              <ul class="list list-marked-check d-inline-block text-left">
                                <li class="list-item">Contributors : ''' + str(mobile_data['contributors']) + '''</li>
                                <li class="list-item">Issues : ''' + str(mobile_data['issues']) + '''</li>
                                <li class="list-item">Stars : ''' + str(mobile_data['stars']) + '''</li>
                                <li class="list-item">Forks : ''' + str(mobile_data['forks']) + '''</li>
                                <li class="list-item disabled">Description : ''' + str(mobile_data['desc']) + '''
                                </li>
                              </ul>
                            </div>
                            <div class="pricing-btn">
                              <button class="btn btn-sm"
                                onclick='window.open("''' + str(mobile_data['repo']) + '''");'>See
                                Repo</button>
                            </div>
                          </div>
                        </article>
        '''
        pro_count = pro_count + 1
  return mobile_body


# print(mobile_view('Python', 4))

var_cats = []
for work in data['works']:
    var_cats.append(work['category'])

var_cats = [i for n, i in enumerate(var_cats) if i not in var_cats[:n]]

var_nav = ""
for ind, nav_cats in enumerate(var_cats):
    tab_id = "tabs-"+str(ind+1)
    if ind == 0:
        var_nav = var_nav + '''
            <li class="nav-item" role="presentation"><a id="custom" class="nav-link show active" href="#''' + tab_id + '''" data-toggle="tab">''' + nav_cats + '''</a></li>
            '''
    else:
        var_nav = var_nav + '''
            <li class="nav-item" role="presentation"><a id="custom" class="nav-link" href="#''' + tab_id + '''" data-toggle="tab">''' + nav_cats + '''</a></li>
            '''


print(var_cats)

var_body = ""
curr_work_index = 0
for ind, i in enumerate(var_cats): # category loop
    var_body = var_body + '''
    <!-- '''+ str(i) +''' -->
    '''
    if ind == 0:
        var_body = var_body + '''
            <div class="tab-pane fade show active" id="tabs-''' + str(ind+1) + '''">
            '''
    else:
        var_body = var_body + '''
            <div class="tab-pane fade" id="tabs-''' + str(ind+1) + '''">
            '''
    var_body = var_body + '''
                    <div class="container position-relative">
          <div class="group-20 d-sm-flex align-items-sm-end justify-content-sm-between text-center">
            <h2></h2>
            <div>
                    <!-- Multi switch-->
                    <div class="switch-text group-25 d-inline-flex align-items-center justify-content-center" id="multiswitch">
                      <div><span class="switch-text-left biggest">Detailed View</span><span class="switch-text-right biggest ml-2 border-left pl-2">Normal View</span></div>
                            <div class="switch-toggle-modern" data-multi-switch='{"targets":"#multiswitch, #pricing-group","state":true}'>
                              <div class="guide"></div>
                              <div class="slider">
                                <div class="slider-dot"></div>
                                <div class="slider-dot"></div>
                              </div>
                            </div>
                    </div>
            </div>
          </div>

          <div class="pricing-group offset-xs" id="pricing-group">'''

    curr_cat_count = 0
    for work in data['works']:
      # count of works in category
      if work['category'] == i:
        curr_cat_count = curr_cat_count + 1
    
    # calculate number of rows required
    num_rows = math.ceil(curr_cat_count/3)
       
    work_count = 0
    row_count = 1
    project_count = 1
    for work in data['works']:
      if work['category'] == i:
        work_count = work_count + 1
        if work_count > 3:
          work_count = 1
          row_count = row_count + 1        

        if work_count == 1:
          if row_count > 1:
            if row_count == 2:
              var_body = var_body + mobile_view(i, project_count)
            var_body = var_body + '''</div>'''
            var_body = var_body + '''
            <!-- Row '''+ str(row_count) +''' -->
                <div class="owl-carousel owl-style-1 owl-item-end pc-custom" data-owl="{&quot;loop&quot;:false,&quot;mouseDrag&quot;:false,&quot;dots&quot;:true,&quot;autoplay&quot;:false,&quot;responsive&quot;:{&quot;768&quot;:{&quot;items&quot;:2},&quot;992&quot;:{&quot;items&quot;:3},&quot;1600&quot;:{&quot;items&quot;:3,&quot;margin&quot;:90}}}">
            '''
          else:
            var_body = var_body + '''
            <!-- Row '''+ str(row_count) +''' -->
                <div class="owl-carousel owl-style-1 owl-item-end" data-owl="{&quot;loop&quot;:false,&quot;mouseDrag&quot;:false,&quot;dots&quot;:true,&quot;autoplay&quot;:false,&quot;responsive&quot;:{&quot;768&quot;:{&quot;items&quot;:2},&quot;992&quot;:{&quot;items&quot;:3},&quot;1600&quot;:{&quot;items&quot;:3,&quot;margin&quot;:90}}}">
            '''
        var_header = ""
        if work['header']:
          var_header = '''<div class="pricing-badge">'''+ str(work['header']) +'''</div>'''
        var_scope = ""
        if work['category'] == "Websites":
          var_scope = '''<button class="btn btn-sm"
                                onclick='window.open("''' + str(work['link']) + '''");'>Visit Website</button><br>
                            '''
        var_access_body = '''<li class="list-item">Contributors : ''' + str(work['contributors']) + '''</li>
                            <li class="list-item">Issues : ''' + str(work['issues']) + '''</li>
                            <li class="list-item">Stars : ''' + str(work['stars']) + '''</li>
                            <li class="list-item">Forks : ''' + str(work['forks']) + '''</li>
                            <li class="list-item disabled">Description : ''' + str(work['desc']) + '''</li>'''
        if work['Access'] == 1:
          var_scope = var_scope + '''<button class="btn btn-sm" data-modal-trigger="{&quot;target&quot;:&quot;#modal&quot;}">See Repo</button>'''
          var_access_body = '''<li class="list-item disabled">This is a Private Repo !</li>'''
        else:
          var_scope = var_scope + '''<button class="btn btn-sm" onclick='window.open("''' + str(work['repo']) + '''");'>See Repo</button>'''
        var_body = var_body + '''
        <!-- Project '''+str(project_count)+''' -->
                    <article class="pricing pricing-primary block block-sm block-center" data-animate='{"class":"fadeInUp"}'>''' + var_header +  '''<div class="pricing-body">
                        <div class="pricing-title biggest h2">''' + str(work['name']) + '''</div>
                        <img src="''' + str(work['logo']) + '''" loading="lazy">
                        <div class="pricing-divider">
                          <hr class="divider">
                        </div>
                        <div class="pricing-list pricing-year">
                          
                          <ul class="list list-marked-check d-inline-block text-left">
                            '''+ var_access_body +'''
                          </ul>
                        </div>
                        <div class="pricing-btn">
                          '''+ var_scope +'''
                        </div>
                      </div>
                    </article>
        '''
        project_count = project_count + 1
    var_body = var_body + '''</div>
          </div>
        </div>
                  </div>'''

# print(var_body)


code_workpage='''
<!DOCTYPE html>
<html lang="en" id="zoom_ele">
  <head>
    <title>Abhijith Udayakumar | Portfolio - Works</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <script src="components/cdn/3ts2ksMwXvKRuG480KNifJ2_JNM.js"></script><link rel="icon" href="media/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="components/base/base-2.css">

    <link rel="preload" as="image" href="media/lang/c.png">
    <link rel="preload" as="image" href="media/lang/cpp.png">
    <link rel="preload" as="image" href="media/lang/csharp.png">
    <link rel="preload" as="image" href="media/lang/dart.png">
    <link rel="preload" as="image" href="media/lang/java.png">
    <link rel="preload" as="image" href="media/lang/jupyter.png">
    <link rel="preload" as="image" href="media/lang/kotlin.png">
    <link rel="preload" as="image" href="media/lang/python.png">
    <link rel="preload" as="image" href="media/lang/vb.png">

    <link rel="preload" as="image" href="media/webs/1.png">
    <link rel="preload" as="image" href="media/webs/2.png">
    <link rel="preload" as="image" href="media/webs/3.png">
    <link rel="preload" as="image" href="media/webs/4.png">
    <link rel="preload" as="image" href="media/webs/5.png">
    <link rel="preload" as="image" href="media/webs/6.png">
    <link rel="preload" as="image" href="media/webs/7.png">
    <link rel="preload" as="image" href="media/webs/8.png">
    <link rel="preload" as="image" href="media/webs/9.png">
    <link rel="preload" as="image" href="media/webs/10.gif">
    <link rel="preload" as="image" href="media/webs/11.png">
    <link rel="preload" as="image" href="media/webs/12.png">
    <link rel="preload" as="image" href="media/webs/13.png">
    <link rel="preload" as="image" href="media/webs/14.png">

    <script src="components/base/core.min.js"></script>
    <script src="components/base/script.js"></script>
    <style type="text/css">
    	#custom.active{
    		color: #354471 !important;
    	}
    	@media only screen and (max-width: 1000px) {
	    	.pc-custom{
	    		display: none !important;
	    	}
    	}
    	@media only screen and (min-width: 1000px) {
	    	.mobile-custom{
	    		display: none !important;
	    	}
	    	.owl-dots
	    	{
	    		display: none !important;
	    	}
	    }
    </style>
    <script type="text/javascript">
    function toggleZoomScreen() {
      var data = document.getElementById('zoom_ele');
       data.style.width = "950px";
       data.style.height = "1080px";
   } 
  </script>
  </head>
  <body>
    <div class="page">
      <!--RD Navbar-->
      <header class="section rd-navbar-wrap">
        <nav class="rd-navbar context">
          <div class="navbar-container">
            <div class="navbar-cell">
              <div class="navbar-panel">
                <button class="navbar-switch" data-multi-switch='{"targets":".rd-navbar","scope":".rd-navbar","isolate":"[data-multi-switch]"}'></button>
                <div class="navbar-logo"><a class="navbar-logo-link" href=""><img class="navbar-logo-inverse" src="media/logo1.svg" alt="Logo" width="300" height="30" loading="lazy"/></a></div>
              </div>
            </div>
            <div class="navbar-spacer"></div>
            <div class="navbar-cell navbar-sidebar">
              <ul class="navbar-navigation rd-navbar-nav fullpage-navigation">
                <li class="navbar-navigation-root-item" data-menuanchor="home"><a class="navbar-navigation-root-link" href="index.html#home">Home</a>
                </li>
                <li class="navbar-navigation-root-item" data-menuanchor="about"><a class="navbar-navigation-root-link" href="index.html#about">About Me</a>
                </li>
                <li class="navbar-navigation-root-item active" data-menuanchor="work"><a class="navbar-navigation-root-link" href="">My Works</a>
                </li>
                
                <li class="navbar-navigation-root-item" data-menuanchor="blog"><a class="navbar-navigation-root-link" href="'''+ data['social']['blog'] +'''">Blog</a>
                </li>
                <li class="navbar-navigation-root-item" data-menuanchor="contacts"><a class="navbar-navigation-root-link" href="index.html#contacts">Contact Me</a>
                </li>
              </ul>
            </div>
            <div class="navbar-cell">
              <div class="navbar-subpanel">
                <div class="navbar-subpanel-item">
                  <button class="navbar-button navbar-info-button mdi-dots-vertical" data-multi-switch='{"targets":".rd-navbar","scope":".rd-navbar","class":"navbar-info-active","isolate":"[data-multi-switch]"}'></button>
                  <div class="navbar-info">
                    <button class="btn btn-sm" onclick="window.location.href='https://raw.githubusercontent.com/Abhijith14/Abhijith14/34c38a706bca4529cf2e59bfec46a63a0fd47e17/Resume.pdf';">Get My Resume</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </nav>
      </header>
      <br>
      <br>
      <br>
      <br>
      <!-- Features-->
      <section class="section section-md pb-lg-0" id="features">
        <div class="container">
          <div class="row row-10">
            <!-- <div class="col-10 col-sm-8 col-lg-6 col-xxl-7 text-center">
            	<img src="media/image-08-698x554.png" alt="" width="698" height="554">
            </div> -->
            <div class="col-lg-10 col-xxl-12 pb-lg-4">
              <div class="title-icon group-20 mt-xxl-2"><span class="icon icon-circle icon-lg icon-style-4 mdi-codepen"></span>
                <h2 onclick="toggleZoomScreen();">My Works</h2>
              </div>
              <div class="tab tab-line">
                <ul class="nav nav-line nav-line-mod-2 bigger active">
                '''+ var_nav +'''
                 <!-- <li class="nav-item" role="presentation"><a id="custom" class="nav-link show active" href="#tabs-1-1" data-toggle="tab">Python</a></li>
                  <li class="nav-item" role="presentation"><a id="custom" class="nav-link" href="#tabs-1-2" data-toggle="tab">Machine Learning</a></li>
                  <li class="nav-item" role="presentation"><a id="custom" class="nav-link" href="#tabs-1-3" data-toggle="tab">Java</a></li>
                  <li class="nav-item" role="presentation"><a id="custom" class="nav-link" href="#tabs-1-4" data-toggle="tab">C/C++</a></li>
                  <li class="nav-item" role="presentation"><a id="custom" class="nav-link" href="#tabs-1-5" data-toggle="tab">C#</a></li>
                  <li class="nav-item" role="presentation"><a id="custom" class="nav-link" href="#tabs-1-6" data-toggle="tab">VB.NET</a></li>
                  <li class="nav-item" role="presentation"><a id="custom" class="nav-link" href="#tabs-1-7" data-toggle="tab">Websites</a></li>
                  <li class="nav-item" role="presentation"><a id="custom" class="nav-link" href="#tabs-1-8" data-toggle="tab">Apps</a></li> -->
                </ul>
                <!-- Tab panes-->
                <div class="tab-content pt-3">
                  
    '''+ var_body +'''       

                </div>
                <!-- Modal-->
        <div class="modal fade" id="modal" tabindex="-1" role="dialog">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-body text-center">
                <h4>Request for <br>Repo Access</h4>
                <!--RD Mailform-->
                <form class="rd-mailform" data-form-output="modal-form-output-global" data-form-type="contact" method="post" action="components/rd-mailform/rd-mailform.php">
                  <div class="form-group">
                    <input class="form-control" type="text" name="name" placeholder="Your name *" data-constraints="@Required">
                  </div>
                  <div class="form-group">
                    <input class="form-control" type="email" name="email" placeholder="Your E-mail *" data-constraints="@Email @Required">
                  </div>
                  <div class="offset-xs">
                    <button class="btn btn-block" type="submit">Send Request</button>
                  </div>
                  <br>
                  <span>This repo has private scope.</span>
                </form>
              </div>
              <button class="close" type="button" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            </div>
          </div>
        </div>

        <div class="form-output snackbar snackbar-secondary" id="modal-form-output-global"></div>
              </div>
            </div>
          </div>
        </div>
      </section>

      
      
      <!-- Get in touch-->
      <section class="section section-xl position-relative" id="contacts">
        <div class="bg-layer-2">
          <svg class="image-svg" width="1920" height="792" viewBox="0 0 1920 792" fill="none">
            <path d="M1305 120.5L-4.12635e-05 120.5L-5.1798e-05 6.10352e-05L1920 -0.000106817L1920 592.5L1510 592.5C1452.01 592.5 1405 545.49 1405 487.5L1405 220.5C1405 165.271 1360.23 120.5 1305 120.5Z" fill="#DEEBF7"></path>
          </svg>
        </div>
        <div class="container">
          <div class="row row-30 align-items-xl-center justify-content-xxl-between">
            <div class="col-lg-6">
              <h2>Get in Touch</h2>
              <p class="bigger op-6">Have a question about our app? Don’t hesitate to contact us directly using the form on this page or by visiting our office.</p>
              <form class="rd-mailform mr-xxl-5" data-form-output="form-output-global" data-form-type="contact" method="post" action="components/rd-mailform/rd-mailform.php">
                <div class="row row-30">
                  <div class="col-xs-6">
                    <div class="form-group">
                      <input class="form-control" type="text" name="name" placeholder="Your name *" data-constraints="@Required">
                    </div>
                  </div>
                  <div class="col-xs-6">
                    <div class="form-group">
                      <input class="form-control" type="email" name="email" placeholder="Your e-mail address *" data-constraints="@Email @Required">
                    </div>
                  </div>
                  <div class="col-12">
                    <div class="form-group">
                      <textarea class="form-control" name="question" placeholder="Your question" rows="5" data-constraints="@Required"></textarea>
                    </div>
                  </div>
                </div>
                <div class="offset-sm group-40 d-flex flex-wrap flex-xs-nowrap align-items-center">
                  <button class="btn" type="submit">Send Message</button>
                        <!-- Checkbox-->
                        <div class="custom-control custom-checkbox">
                          <input class="custom-control-input" type="checkbox" id="check1">
                          <label class="custom-control-label" for="check1">Get weekly news and updates
                          </label>
                        </div>
                </div>
              </form>
            </div>
            <div class="col-lg-6">
              <div class="box px-xl-3 px-xxl-4">
                <div class="row row-30">
                  <div class="col-md-6 col-lg-12 col-xl-6">
                    <h4>Reference:</h4>
                    <div class="group-30 offset-sm">
                      <a class="btn btn-app pl-1" href="#">
                        <span class="btn-icon icon icon-round icon-sm icon-primary icon-style-3 mdi-code-greater-than-or-equal"></span>
                        <span>Kaggle.com</span>
                      </a>
                      <a class="btn btn-app pl-1" href="#">
                        <span class="btn-icon icon icon-round icon-sm icon-primary icon-style-3 mdi-github-box"></span>
                        <span>GitHub.com</span>
                      </a>
                    </div>
                  </div>
                  <div class="col-md-6 col-lg-12 col-xl-6">
                    <h4>Contacts:</h4>
                    <table class="table table-sm table-responsive-xl table-no-bordered bigger">
                      <tbody>
                        <tr>
                          <td class="text-right op-6 pl-0 align-middle">Ph.</td>
                          <td class="biggest"><a class="link-inherit" href="tel:919946883500">+91 9946883500</a></td>
                        </tr>
                        <tr>
                          <td class="text-right op-6 pl-0">Mail.</td>
                          <td>
                          	<a class="link-inherit" href="mailto:abhijithukzm@gmail.com" style="font-size: 14px;">abhijithukzm@gmail.com</a>
                          	<br>
                          	<a class="link-inherit" href="mailto:buddy.assistant14@gmail.com" style="font-size: 14px;">buddy.assistant14@gmail.com</a></td>
                        </tr>
                        <!-- <tr>
                          <td class="text-right op-6 pl-0">Office.</td>
                          <td>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</td>
                        </tr> -->
                      </tbody>
                    </table>
                  </div>
                </div>
                <hr class="divider">
                <div class="group-20 d-flex flex-wrap align-items-center justify-content-between">
                  <div>
                          <!-- List social-->
                          <ul class="list list-social">
                            <li class="list-social-item"><a class="icon icon-circle icon-md icon-style-1 mdi-facebook" href="'''+ data['social']['Facebook'] +'''"></a></li>
                            <li class="list-social-item"><a class="icon icon-circle icon-md icon-style-1 mdi-twitter" href="'''+ data['social']['Twitter'] +'''"></a></li>
                            <li class="list-social-item"><a class="icon icon-circle icon-md icon-style-1 mdi-instagram" href="'''+ data['social']['Instagram'] +'''"></a></li>
                          </ul>
                  </div>
                  <div>
                          <!-- Copyright-->
                          <p class="rights bigger"><span>&copy; 2021.&nbsp;</span><span></span><span> All rights reserved</span></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="form-output snackbar snackbar-secondary" id="form-output-global"></div>
      </section>
    </div>
    <!-- Modal-->
    <div class="modal fade" id="modal-login" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-body text-center">
            <h3>Log In</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing</p>
            <form class="rd-mailform">
              <div class="form-group">
                <input class="form-control" type="text" name="name" placeholder="Your name *" data-constraints="@Required">
              </div>
              <div class="form-group">
                <input class="form-control" type="password" name="password" placeholder="Password *" data-constraints="@Required">
              </div>
              <div class="offset-xxs group-40 d-flex flex-wrap flex-xs-nowrap align-items-center">
                <button class="btn btn-block" type="submit">Log in</button>
              </div>
            </form>
          </div>
          <button class="close" type="button" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
        </div>
      </div>
    </div>
    <!-- Preloader-->
    <div class="preloader">
      <div class="preloader-inner">
        <div class="preloader-dot"></div>
        <div class="preloader-dot"></div>
        <div class="preloader-dot"></div>
        <div class="preloader-dot"></div>
      </div>
    </div>
  </body>
</html>'''



save(code_homepage, './index.html')
save(code_workpage, './work.html')

# Closing json
f.close()
