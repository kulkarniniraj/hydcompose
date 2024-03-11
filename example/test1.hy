(container
    :image "mariadb"
    :name "mariadb"
    :ports [(dict :host 13306 :container 3306)]
    :volumes [(dict :host "/home/niraj/Documents/tmp/mariadb" 
                   :container "/var/lib")]
    :env [(dict :key "MARIADB_ROOT_PASSWORD"
            :value "test123")])

(container
    :image "flask"
    :name "web-server"
    :ports [(dict :host 8080 :container 80)]
    :depends-on [(dict :name "mariadb" :event "after-start")]
    )

(container
    :image "flask"
    :name "service1"
    :ports [(dict :host 8081 :container 80)]
    :depends-on [(dict :name "mariadb" :event "after-start")]
    )    