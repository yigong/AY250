


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>python-seminar/Homeworks/hw_4-machine-learning-parallel-strawman.py at master · profjsb/python-seminar</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="https://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta property="og:image" content="https://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png">
    <meta name="hostname" content="github-fe133-cp1-prd.iad.github.net">
    <meta name="ruby" content="ruby 1.9.3p194-tcs-github-tcmalloc (2012-05-25, TCS patched 2012-05-27, GitHub v1.0.36) [x86_64-linux]">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035/">
    <link rel="xhr-socket" href="/_sockets" />
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="800309FB:2439:796C258:524C7B88" name="octolytics-dimension-request_id" /><meta content="5041832" name="octolytics-actor-id" /><meta content="yigong" name="octolytics-actor-login" /><meta content="35c2da6148f96cf6ed35231af86662c98766655a54b61f372d306aee9548c214" name="octolytics-actor-hash" />
    

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="83lCqgHj5otbMiNjOPAFkarEMI1IxSNrMWCOfqyn7/U=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-33cf54e1c25c41c1bb09506a6e93ef032819ce2c.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-427490d1371388abf1605de546c0161ae2001a1d.css" media="all" rel="stylesheet" type="text/css" />
    

    

      <script src="https://github.global.ssl.fastly.net/assets/frameworks-4e5aeedcc7a86dcff8294cb84644a333b46202a2.js" type="text/javascript"></script>
      <script src="https://github.global.ssl.fastly.net/assets/github-f9acb9ba6715dc87635b1172f2ea8d036668952e.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="ce99b552d7a6b51a2d2960b4b5576973">

        <link data-pjax-transient rel='permalink' href='/profjsb/python-seminar/blob/e092f48aa7135e5f0e17b165366ac3ce7e04d2d2/Homeworks/hw_4-machine-learning-parallel-strawman.py'>
  <meta property="og:title" content="python-seminar"/>
  <meta property="og:type" content="githubog:gitrepository"/>
  <meta property="og:url" content="https://github.com/profjsb/python-seminar"/>
  <meta property="og:image" content="https://github.global.ssl.fastly.net/images/gravatars/gravatar-user-420.png"/>
  <meta property="og:site_name" content="GitHub"/>
  <meta property="og:description" content="python-seminar - Python Seminar Course at UC Berkeley (AY 250)"/>

  <meta name="description" content="python-seminar - Python Seminar Course at UC Berkeley (AY 250)" />

  <meta content="480799" name="octolytics-dimension-user_id" /><meta content="profjsb" name="octolytics-dimension-user_login" /><meta content="5518536" name="octolytics-dimension-repository_id" /><meta content="profjsb/python-seminar" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="5518536" name="octolytics-dimension-repository_network_root_id" /><meta content="profjsb/python-seminar" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/profjsb/python-seminar/commits/master.atom" rel="alternate" title="Recent Commits to python-seminar:master" type="application/atom+xml" />

  </head>


  <body class="logged_in  env-production linux vis-public  page-blob">
    <div class="wrapper">
      
      
      


      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/">
  <span class="mega-octicon octicon-mark-github"></span>
</a>

    
    <a href="/notifications" class="notification-indicator tooltipped downwards" data-gotokey="n" title="You have unread notifications">
        <span class="mail-status unread"></span>
</a>

      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    data-username="yigong"
      data-repo="profjsb/python-seminar"
      data-branch="master"
      data-sha="b24a57800e8b3bfb26894da58d3c94d3cd01f247"
  >

    <input type="hidden" name="nwo" value="profjsb/python-seminar" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    


  <ul id="user-links">
    <li>
      <a href="/yigong" class="name">
        <img height="20" src="https://2.gravatar.com/avatar/7f25913ee4258bc0389b0c6724ae03ac?d=https%3A%2F%2Fidenticons.github.com%2F5b2212dfd54e2f3a4b0241d91dfcb1d9.png&amp;s=140" width="20" /> yigong
      </a>
    </li>

      <li>
        <a href="/new" id="new_repo" class="tooltipped downwards" title="Create a new repo" aria-label="Create a new repo">
          <span class="octicon octicon-repo-create"></span>
        </a>
      </li>

      <li>
        <a href="/settings/profile" id="account_settings"
          class="tooltipped downwards"
          aria-label="Account settings "
          title="Account settings ">
          <span class="octicon octicon-tools"></span>
        </a>
      </li>
      <li>
        <a class="tooltipped downwards" href="/logout" data-method="post" id="logout" title="Sign out" aria-label="Sign out">
          <span class="octicon octicon-log-out"></span>
        </a>
      </li>

  </ul>

<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo-create"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>



    <li class="section-title">
      <span title="profjsb/python-seminar">This repository</span>
    </li>
    <li>
      <a href="/profjsb/python-seminar/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
    </li>
</ul>

</div>


    
  </div>
</div>

      

      




          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="83lCqgHj5otbMiNjOPAFkarEMI1IxSNrMWCOfqyn7/U=" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="5518536" />

    <div class="select-menu js-menu-container js-select-menu">
        <a class="social-count js-social-count" href="/profjsb/python-seminar/watchers">
          46
        </a>
      <span class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0">
        <span class="js-select-button">
          <span class="octicon octicon-eye-watch"></span>
          Watch
        </span>
      </span>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container" role="menu">

            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for discussions in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-watch"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
  
<div class="js-toggler-container js-social-container starring-container ">
  <a href="/profjsb/python-seminar/unstar" class="minibutton with-count js-toggler-target star-button starred upwards" title="Unstar this repo" data-remote="true" data-method="post" rel="nofollow">
    <span class="octicon octicon-star-delete"></span><span class="text">Unstar</span>
  </a>
  <a href="/profjsb/python-seminar/star" class="minibutton with-count js-toggler-target star-button unstarred upwards" title="Star this repo" data-remote="true" data-method="post" rel="nofollow">
    <span class="octicon octicon-star"></span><span class="text">Star</span>
  </a>
  <a class="social-count js-social-count" href="/profjsb/python-seminar/stargazers">65</a>
</div>

  </li>


        <li>
          <a href="/profjsb/python-seminar/fork" class="minibutton with-count js-toggler-target fork-button lighter upwards" title="Fork this repo" rel="facebox nofollow">
            <span class="octicon octicon-git-branch-create"></span><span class="text">Fork</span>
          </a>
          <a href="/profjsb/python-seminar/network" class="social-count">27</a>
        </li>


</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/profjsb" class="url fn" itemprop="url" rel="author"><span itemprop="title">profjsb</span></a></span
          ><span class="repohead-name-divider">/</span><strong
          ><a href="/profjsb/python-seminar" class="js-current-repository js-repo-home-link">python-seminar</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">

      <div class="repository-with-sidebar repo-container ">

        <div class="repository-sidebar">
            

<div class="repo-nav repo-nav-full js-repository-container-pjax js-octicon-loaders">
  <div class="repo-nav-contents">
    <ul class="repo-menu">
      <li class="tooltipped leftwards" title="Code">
        <a href="/profjsb/python-seminar" aria-label="Code" class="js-selected-navigation-item selected" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /profjsb/python-seminar">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped leftwards" title="Issues">
          <a href="/profjsb/python-seminar/issues" aria-label="Issues" class="js-selected-navigation-item js-disable-pjax" data-gotokey="i" data-selected-links="repo_issues /profjsb/python-seminar/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>1</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped leftwards" title="Pull Requests"><a href="/profjsb/python-seminar/pulls" aria-label="Pull Requests" class="js-selected-navigation-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /profjsb/python-seminar/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped leftwards" title="Wiki">
          <a href="/profjsb/python-seminar/wiki" aria-label="Wiki" class="js-selected-navigation-item " data-pjax="true" data-selected-links="repo_wiki /profjsb/python-seminar/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="repo-menu-separator"></div>
    <ul class="repo-menu">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/profjsb/python-seminar/pulse" aria-label="Pulse" class="js-selected-navigation-item " data-pjax="true" data-selected-links="pulse /profjsb/python-seminar/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/profjsb/python-seminar/graphs" aria-label="Graphs" class="js-selected-navigation-item " data-pjax="true" data-selected-links="repo_graphs repo_contributors /profjsb/python-seminar/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/profjsb/python-seminar/network" aria-label="Network" class="js-selected-navigation-item js-disable-pjax" data-selected-links="repo_network /profjsb/python-seminar/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

            <div class="only-with-full-nav">
              

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/profjsb/python-seminar.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/profjsb/python-seminar.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><strong>SSH</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="git@github.com:profjsb/python-seminar.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="git@github.com:profjsb/python-seminar.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/profjsb/python-seminar" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/profjsb/python-seminar" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="octicon help tooltipped upwards" title="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>



              <a href="/profjsb/python-seminar/archive/master.zip"
                 class="minibutton sidebar-button"
                 title="Download this repository as a zip file"
                 rel="nofollow">
                <span class="octicon octicon-cloud-download"></span>
                Download ZIP
              </a>
            </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:04e7e283c9c72a2fd5754bc0e46d21ae -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/profjsb/python-seminar/find/master" data-pjax data-hotkey="t" class="js-show-file-finder" style="display:none">Show File Finder</a>

<div class="file-navigation">
  


<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    role="button" aria-label="Switch branches or tags" tabindex="0">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/profjsb/python-seminar/blob/gh-pages/Homeworks/hw_4-machine-learning-parallel-strawman.py"
                 data-name="gh-pages"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="gh-pages">gh-pages</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/profjsb/python-seminar/blob/master/Homeworks/hw_4-machine-learning-parallel-strawman.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/profjsb/python-seminar/tree/fall2012/Homeworks/hw_4-machine-learning-parallel-strawman.py"
                 data-name="fall2012"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="fall2012">fall2012</a>
            </div> <!-- /.select-menu-item -->
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/profjsb/python-seminar" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">python-seminar</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/profjsb/python-seminar/tree/master/Homeworks" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">Homeworks</span></a></span><span class="separator"> / </span><strong class="final-path">hw_4-machine-learning-parallel-strawman.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="Homeworks/hw_4-machine-learning-parallel-strawman.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/profjsb/python-seminar/contributors/master/Homeworks/hw_4-machine-learning-parallel-strawman.py">
    Fetching contributors…

    <div class="participation">
      <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
      <p class="loader-error">Cannot retrieve contributors at this time</p>
    </div>
  </div>

<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
          <span>83 lines (71 sloc)</span>
        <span>3.205 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
                <a class="minibutton tooltipped upwards"
                   title="Clicking this button will automatically fork this project so you can edit the file"
                   href="/profjsb/python-seminar/edit/master/Homeworks/hw_4-machine-learning-parallel-strawman.py"
                   data-method="post" rel="nofollow">Edit</a>
          <a href="/profjsb/python-seminar/raw/master/Homeworks/hw_4-machine-learning-parallel-strawman.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/profjsb/python-seminar/blame/master/Homeworks/hw_4-machine-learning-parallel-strawman.py" class="button minibutton ">Blame</a>
          <a href="/profjsb/python-seminar/commits/master/Homeworks/hw_4-machine-learning-parallel-strawman.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
            <a class="minibutton danger empty-icon tooltipped downwards"
               href="/profjsb/python-seminar/delete/master/Homeworks/hw_4-machine-learning-parallel-strawman.py"
               title="Fork this project and delete file"
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">
            Delete
          </a>
      </div><!-- /.actions -->

    </div>
        <div class="blob-wrapper data type-python js-blob-data">
        <table class="file-code file-diff">
          <tr class="file-code-line">
            <td class="blob-line-nums">
              <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>

            </td>
            <td class="blob-line-code">
                    <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python</span></div><div class='line' id='LC2'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC3'><span class="sd">AY 250 - Scientific Research Computing with Python</span></div><div class='line' id='LC4'><span class="sd">Homework Assignment 4 - Parallel Feature Extraction Example</span></div><div class='line' id='LC5'><span class="sd">Author: Christopher Klein, Joshua Bloom</span></div><div class='line' id='LC6'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC7'><span class="kn">from</span> <span class="nn">os</span> <span class="kn">import</span> <span class="n">listdir</span></div><div class='line' id='LC8'><span class="kn">from</span> <span class="nn">multiprocessing</span> <span class="kn">import</span> <span class="n">Pool</span><span class="p">,</span> <span class="n">cpu_count</span></div><div class='line' id='LC9'><span class="kn">from</span> <span class="nn">pylab</span> <span class="kn">import</span> <span class="n">imread</span></div><div class='line' id='LC10'><span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">time</span></div><div class='line' id='LC11'><br/></div><div class='line' id='LC12'><span class="c">## CHANGE THIS NEXT LINE!</span></div><div class='line' id='LC13'><span class="n">MYDIRECTORY</span> <span class="o">=</span> <span class="s">&quot;/Users/jbloom/Classes/ay250-py4sci/week4/50_categories&quot;</span></div><div class='line' id='LC14'><br/></div><div class='line' id='LC15'><span class="c"># FUNCTION DEFINITIONS</span></div><div class='line' id='LC16'><span class="c"># Quick function to divide up a large list into multiple small lists, </span></div><div class='line' id='LC17'><span class="c"># attempting to keep them all the same size. </span></div><div class='line' id='LC18'><span class="k">def</span> <span class="nf">split_seq</span><span class="p">(</span><span class="n">seq</span><span class="p">,</span> <span class="n">size</span><span class="p">):</span></div><div class='line' id='LC19'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">newseq</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC20'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">splitsize</span> <span class="o">=</span> <span class="mf">1.0</span><span class="o">/</span><span class="n">size</span><span class="o">*</span><span class="nb">len</span><span class="p">(</span><span class="n">seq</span><span class="p">)</span></div><div class='line' id='LC21'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">size</span><span class="p">):</span></div><div class='line' id='LC22'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">newseq</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">seq</span><span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">i</span><span class="o">*</span><span class="n">splitsize</span><span class="p">)):</span></div><div class='line' id='LC23'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">int</span><span class="p">(</span><span class="nb">round</span><span class="p">((</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">splitsize</span><span class="p">))])</span></div><div class='line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">newseq</span></div><div class='line' id='LC25'><span class="c"># Our simple feature extraction function. It takes in a list of image paths, </span></div><div class='line' id='LC26'><span class="c"># does some measurement on each image, then returns a list of the image paths</span></div><div class='line' id='LC27'><span class="c"># paired with the results of the feature measurement.</span></div><div class='line' id='LC28'><span class="k">def</span> <span class="nf">extract_features</span><span class="p">(</span><span class="n">image_path_list</span><span class="p">):</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">feature_list</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">image_path</span> <span class="ow">in</span> <span class="n">image_path_list</span><span class="p">:</span></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">image_array</span> <span class="o">=</span> <span class="n">imread</span><span class="p">(</span><span class="n">image_path</span><span class="p">)</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">feature</span> <span class="o">=</span> <span class="n">image_array</span><span class="o">.</span><span class="n">size</span> <span class="c"># This feature is simple. You can modify this</span></div><div class='line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># code to produce more complicated features and to produce multiple</span></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># features in one function call.</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">feature_list</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">image_path</span><span class="p">,</span> <span class="n">feature</span><span class="p">])</span></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">feature_list</span></div><div class='line' id='LC37'><br/></div><div class='line' id='LC38'><br/></div><div class='line' id='LC39'><br/></div><div class='line' id='LC40'><span class="c">### Main program starts here ###################################################</span></div><div class='line' id='LC41'><span class="c"># We first collect all the local paths to all the images in one list</span></div><div class='line' id='LC42'><span class="n">image_paths</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC43'><span class="n">categories</span> <span class="o">=</span> <span class="n">listdir</span><span class="p">(</span><span class="n">MYDIRECTORY</span><span class="p">)</span></div><div class='line' id='LC44'><span class="k">for</span> <span class="n">category</span> <span class="ow">in</span> <span class="n">categories</span><span class="p">:</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">image_names</span> <span class="o">=</span> <span class="n">listdir</span><span class="p">(</span><span class="n">MYDIRECTORY</span>  <span class="o">+</span> <span class="s">&quot;/&quot;</span> <span class="o">+</span> <span class="n">category</span><span class="p">)</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">image_names</span><span class="p">:</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">image_paths</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">MYDIRECTORY</span> <span class="o">+</span> <span class="s">&quot;/&quot;</span> <span class="o">+</span> <span class="n">category</span> <span class="o">+</span> <span class="s">&quot;/&quot;</span> <span class="o">+</span> <span class="n">name</span><span class="p">)</span></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'><span class="k">print</span> <span class="p">(</span><span class="s">&quot;There should be 4244 images, actual number is &quot;</span> <span class="o">+</span> </div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">str</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">image_paths</span><span class="p">))</span> <span class="o">+</span> <span class="s">&quot;.&quot;</span><span class="p">)</span></div><div class='line' id='LC51'><br/></div><div class='line' id='LC52'><span class="c"># Then, we run the feature extraction function using multiprocessing.Pool so </span></div><div class='line' id='LC53'><span class="c"># so that we can parallelize the process and run it much faster.</span></div><div class='line' id='LC54'><span class="n">numprocessors</span> <span class="o">=</span> <span class="n">cpu_count</span><span class="p">()</span> <span class="c"># To see results of parallelizing, set numprocessors</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># to less than cpu_count().</span></div><div class='line' id='LC56'><span class="c"># numprocessors = 1</span></div><div class='line' id='LC57'><br/></div><div class='line' id='LC58'><span class="c"># We have to cut up the image_paths list into the number of processes we want to</span></div><div class='line' id='LC59'><span class="c"># run. </span></div><div class='line' id='LC60'><span class="n">split_image_paths</span> <span class="o">=</span> <span class="n">split_seq</span><span class="p">(</span><span class="n">image_paths</span><span class="p">,</span> <span class="n">numprocessors</span><span class="p">)</span></div><div class='line' id='LC61'><br/></div><div class='line' id='LC62'><span class="c"># Ok, this block is where the parallel code runs. We time it so we can get a </span></div><div class='line' id='LC63'><span class="c"># feel for the speed up.</span></div><div class='line' id='LC64'><span class="n">start_time</span> <span class="o">=</span> <span class="n">time</span><span class="p">()</span></div><div class='line' id='LC65'><span class="n">p</span> <span class="o">=</span> <span class="n">Pool</span><span class="p">(</span><span class="n">numprocessors</span><span class="p">)</span></div><div class='line' id='LC66'><span class="n">result</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">map_async</span><span class="p">(</span><span class="n">extract_features</span><span class="p">,</span> <span class="n">split_image_paths</span><span class="p">)</span></div><div class='line' id='LC67'><span class="n">poolresult</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">get</span><span class="p">()</span></div><div class='line' id='LC68'><span class="n">end_time</span> <span class="o">=</span> <span class="n">time</span><span class="p">()</span></div><div class='line' id='LC69'><br/></div><div class='line' id='LC70'><span class="c"># All done, print timing results.</span></div><div class='line' id='LC71'><span class="k">print</span> <span class="p">(</span><span class="s">&quot;Finished extracting features. Total time: &quot;</span> <span class="o">+</span> </div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">str</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">end_time</span><span class="o">-</span><span class="n">start_time</span><span class="p">,</span> <span class="mi">3</span><span class="p">))</span> <span class="o">+</span> <span class="s">&quot; s, or &quot;</span> <span class="o">+</span> </div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">str</span><span class="p">(</span> <span class="nb">round</span><span class="p">(</span> <span class="p">(</span><span class="n">end_time</span><span class="o">-</span><span class="n">start_time</span><span class="p">)</span><span class="o">/</span><span class="nb">len</span><span class="p">(</span><span class="n">image_paths</span><span class="p">),</span> <span class="mi">5</span> <span class="p">)</span> <span class="p">)</span> <span class="o">+</span> <span class="s">&quot; s/image.&quot;</span><span class="p">)</span></div><div class='line' id='LC74'><span class="c"># This took about 10-11 seconds on my 2.2 GHz, Core i7 MacBook Pro. It may also</span></div><div class='line' id='LC75'><span class="c"># be affected by hard disk read speeds.</span></div><div class='line' id='LC76'><br/></div><div class='line' id='LC77'><span class="c"># To tidy-up a bit, we loop through the poolresult to create a final list of</span></div><div class='line' id='LC78'><span class="c"># the feature extraction results for all images.</span></div><div class='line' id='LC79'><span class="n">combined_result</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC80'><span class="k">for</span> <span class="n">single_proc_result</span> <span class="ow">in</span> <span class="n">poolresult</span><span class="p">:</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">single_image_result</span> <span class="ow">in</span> <span class="n">single_proc_result</span><span class="p">:</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">combined_result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">single_image_result</span><span class="p">)</span></div></pre></div>
            </td>
          </tr>
        </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2013 <span title="0.04805s from github-fe133-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/profjsb/python-seminar/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

  </body>
</html>

